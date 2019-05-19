# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    proxy.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akharrou <akharrou@student.42.us.org>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/05/18 15:03:05 by akharrou          #+#    #+#              #
#    Updated: 2019/05/18 19:25:26 by akharrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import signal
import socket
import requests
import threading

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

class proxyServer:

	def __init__(self, config):

		# Shutdown on Crtl+C
		signal.signal(signal.SIGINT, self._shutdown)

		# Set the Socket Configuration
		self.config = config

		# Create a TCP Socket
		self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# Re-use the Socket
		self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		# Bind the Socket to a Public Host, and a Port
		self.serverSocket.bind((config['HOST'], config['PORT']))

		# Become a Server Socket
		self.serverSocket.listen(10)

		print(f'\nProxy Server Status: [LIVE]')
		print(f'Proxy Server running at "http://{HOST}:{PORT}/"')

		# Create a dictionary to Store Clients
		self.__clients = {}

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

	def _shutdown(self, *args):

		self.serverSocket.close()
		print('\nProxy Server Shutting Down.')
		sys.exit(1)

	def _getClientName(self, cliAddress):
		return (cliAddress[1])

	def _getUrl(self, request):

		firstline = request.split(':')[0]
		url = firstline.split(' ')[1]

		return (url)

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

	def proxyThread(self, clientSocket, clientAddress):

		print(f'\nConnection established with {clientAddress[0]} on port {clientAddress[1]}.\n')

		# Obtain the Client's Request
		clientRequest = str(clientSocket.recv(self.config['MAX_REQUEST_LEN']))

		print('————————————————————————CLIENT-REQUEST————————————————————————————\n')
		print(clientRequest, end="\n\n")

		# Obtain the Client's Intended Destination
		url = self._getUrl(clientRequest)

		with requests.Session() as s:

			# Forward the Client's Request to its Intended Destination
			response = s.get(f'http://{url}')

			print('————————————————————————SERVER-RESPONSE————————————————————————————\n')
			print(response.content)
			print('\n—————————————————————————RESPONSE-END————————————————————————————')

			# Forward the Server's Response to the Client
			clientSocket.send(response.content)

			print('Response Successfully Sent.')

		# Close the Socket
		clientSocket.close()

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

	def run(self, config):

		while True:

			try:

				# Establish a Connection
				clientSocket, clientAddress = self.serverSocket.accept()

				# Branch off to another thread
				connThread = threading.Thread(	name   = self._getClientName(clientAddress),
												target = self.proxyThread,
												args   = (clientSocket, clientAddress)  )

				# Turn into a Daemon
				connThread.setDaemon(True)

				# Let the Thread run as a Daemon in the Background
				connThread.start()

			except KeyboardInterrupt:
				shutdown(-1)

		self.serverSocket.close()

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

HOST            = str( input("Proxy Server Hostname: ") )
PORT            = int( input("Proxy Server Port: ") )
MAX_REQUEST_LEN = 4096

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

proxyConfig = {
    "HOST"            : HOST,
    "PORT"            : PORT,
    "MAX_REQUEST_LEN" : MAX_REQUEST_LEN
}

# ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
myProxyServer = proxyServer(proxyConfig)
myProxyServer.run(proxyConfig)
