## Hercules — The Apples of Hesperides

#### How to login to a VM without the needing a password ?


1.  Create public and private keys using `ssh-keygen` on **local-host**

	```
	$> ssh-keygen
	```


2.  Copy the public key to **remote-host** using `ssh-copy-id`

	```
	$> ssh-copy-id -i ~/.ssh/id_rsa.pub <remote-host>
	```

3.  Login to remote-host without entering the password

	```
	$> ssh <remote-host>
	```
