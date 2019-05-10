## Hercules — The Apples of Hesperides

#### How to login to a VM without the need of the password ?


1.  Create public and private keys using `ssh-keygen` on **local-host**

	```
	akharrou@local-host$ ssh-keygen
	```


2.  Copy the public key to **remote-host** using `ssh-copy-id`

	```
	akharrou@local-host$ ssh-copy-id -i ~/.ssh/id_rsa.pub <remote-host>
	```

3.  Login to remote-host without entering the password

	```
	akharrou@local-host$ ssh <remote-host>
	```
