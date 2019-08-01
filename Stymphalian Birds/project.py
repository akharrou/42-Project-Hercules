# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    project.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akharrou <akharrou@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/04/05 12:20:16 by akharrou          #+#    #+#              #
#    Updated: 2019/04/05 18:19:40 by akharrou         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import os

def generate_C_project(project_name, createLib):

	try:

		# """ Directory Creation """

		os.makedirs(f'{project_name}')
		print(f'  create : {project_name}/')

		os.makedirs(f'{project_name}/Sources')
		print(f'  create : {project_name}/Sources/')

		os.makedirs(f'{project_name}/Includes')
		print(f'  create : {project_name}/Includes')

		os.makedirs(f'{project_name}/Tests')
		print(f'  create : {project_name}/Tests/')

		if (createLib == True):
			os.system(f'cp -R ~/Desktop/42-Workspace/Libft/ ./{project_name}/Sources/Libft/')
			print(f'  create : {project_name}/Sources/Lib')


		# """ File Creation """

		with open(f'{project_name}/Makefile', 'w') as f:
			f.write("""
# **************************************************************************** #
#                                                                              #
#                              MAKEFILE FRAMEWORK                              #
#                                                                              #
# **************************************************************************** #

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

CC          =   gcc
CFLAGS      =   -Wall -Wextra -Werror

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

INC_DIR     =   Includes

NAME        =   fillit

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

LIBRARIES   =   libft.a

# — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

SOURCES     =   main.c \

OBJECTS     =   $(SOURCES:.c=.o)

# =============================================================================
#                                                                             #
#                            DO NOT TOUCH THE REST                            #
#                                                                             #
# =============================================================================

all: $(NAME)

$(NAME): $(OBJECTS) $(LIBRARIES)
	@$(CC) $(OBJECTS) $(LIBRARIES)

%.o: %.c
	@$(CC) $(CFLAGS) -I $(INC_DIR) -c $< -o $@
	@echo "Compiling => " $<

# =============================================================================

DEL  =  /bin/rm -rf

clean:
	@$(DEL) $(shell find . -name '*.o')

fclean: clean
	@$(DEL) $(NAME)

re: fclean all

# =============================================================================

nc:
	@echo && echo $(GREEN) "Checking Norme -- Source Files:" && echo $(WHITE);
	@norminette $(shell find . -name '*.c')

nh:
	@echo && echo $(GREEN) "Checking Norme -- Header Files:" && echo $(WHITE);
	@norminette $(shell find . -name '*.h')

na: nh nc

# =============================================================================

GREEN =  "\033[1;32m"
WHITE =  "\033[1;37m"

# =============================================================================

.PHONY: all clean fclean re nc nh na

# =============================================================================

""")
	except Exception as e:
		print('\nOops, something went wrong...')


def generate_website_project(project_name):

	try:

		# """ Directory Creation """

		os.makedirs(f'{project_name}')
		print(f'  create : {project_name}/')

		os.makedirs(f'{project_name}/bin')
		print(f'  create : {project_name}/bin/')

		os.makedirs(f'{project_name}/public/html')
		print(f'  create : {project_name}/public/html/')

		os.makedirs(f'{project_name}/public/css')
		print(f'  create : {project_name}/public/css/')

		os.makedirs(f'{project_name}/public/javascript')
		print(f'  create : {project_name}/public/javascript/')

		os.makedirs(f'{project_name}/public/assets')
		print(f'  create : {project_name}/public/assets/')

		os.makedirs(f'{project_name}/routes')
		print(f'  create : {project_name}/routes/')

		os.makedirs(f'{project_name}/utils')
		print(f'  create : {project_name}/utils/')


		# """ File Creation """

		with open(f'{project_name}/bin/www', 'w') as f:
			f.write("""
/* Module Dependencies */
var app = require('../app');
var http = require('http');

/* Set Port */
var PORT = 8080;
app.set('port', '8080');

/* Create the HTTP server. */
var server = http.createServer(app);

/* Start the Server */
server.listen(PORT, () => {
		console.log("Server Status: [LIVE]");
		console.log(`Server running at 'http://localhost:$\{PORT\}/'`);
});""")

		with open(f'{project_name}/routes/index.js', 'w') as f:
			f.write("""
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
res.render('index', { title: 'Express' });
});

	module.exports = router;""")

		with open(f'{project_name}/app.js', 'w') as f:
			f.write("""

// Application Dependencies
// ===============================================================================

/* Import Application Dependencies */
var path = require('path');
var express = require('express');
const bodyParser = require('body-parser');
const session = require('express-session');

/* Create/Import Routes */
var userRouter = require('./routes/users');
var indexRouter = require('./routes/index');
var adminRouter = require('./routes/admin');


// Initialize Application Server
// ===============================================================================
var app = express();


// Add MiddleWare
// ===============================================================================

// Set Path to Static HTML Pages
app.use(express.static(path.join(__dirname, 'public/html/')));

// Request Body Parsers
app.use(express.json());
app.use(express.urlencoded(\{ extended: false \}));

// Use 'express-session' to Automatically Create Cookies
var sess_options = {
		secret: 'whippersnapper' + Math.floor((Math.random() * 1000000000000) + 1),
		cookie: \{ maxAge: 60000 \}
};
app.use(session(sess_options));

// Set Created Routes
app.use('/', indexRouter);
app.use('/user', userRouter);
app.use('/admin', adminRouter);


// Export
// ===============================================================================

module.exports=app; """)

		# """ Install Required Packages """
		os.system(f'cp ~/Desktop/package-lock.json ./{project_name}')

		# """ Install Required Packages """
		# os.system(f'npm install')

		print(f'\n  Process Completed !\n')

	except Exception as e:
		print('\nOops, something went wrong...')


def main():

	try:
		if len(sys.argv) == 1 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
			print("""NAME
     project -- initialize a project

SYNOPSIS
	 python project [-h] [name] [--website] [-l]

DESCRIPTION
     Automates the setting up of a project.


-h, --help
	Displays this page, showing a help section.

-l
	Specify whether to include libft in your C project.

--website
	Specify that the project is a website project.
	If not specified a C project is the default
	project that is spawned.""")
			return

	except Exception as f:
		project_name = 'myApp'

	try:
		project_name = sys.argv[1];
	except Exception as f:
		project_name = 'myApp'

	website = False
	for arg in sys.argv:
		if arg == '--website':
			website = True

	createLib = False
	for arg in sys.argv:
		if arg == '-l':
			createLib = True

	print(f'\n  Creating {project_name} !\n')

	if (website == False):
		generate_C_project(project_name, createLib)
	else:
		generate_website_project(project_name)

	# """ Initalize Git Repository & Create Git Ignore File """
	os.chdir(project_name)
	os.system(f'git init ; touch .gitignore')


if __name__ == '__main__':
	main()
