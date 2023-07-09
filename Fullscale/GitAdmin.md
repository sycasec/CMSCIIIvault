[[fullscale_root]]

# Git Administration
```toc
```

# Serving Git
## Git Protocol
### Local Protocol
- working with git on a server using its filesystem
- team has shared file server
- authentication and authorization is handled by local sysadmin
- can be inefficient if volumes are mounted remotely (in a network)
- uses a file path when cloning a repo
	- `git clone file:///var/repositories/sample_project.git`
### Remote Protocol
- working with git on a separate server
- #### SSH connection
	- uses SSH auth
	- encrypts all git traffic to and from server
	- requires authenticated user
	- most used of all git protocols
	- SSH syntax
		- `git clone ssh://david@gitserver/repos/sample_project.git`
		- `git clone david@gitserver:repos/sample_project.git`
- #### HTTP(s) connection
	- share git repo through web server through http
	- requires configuring a web server
	- encrypts traffic if using HTTPS
	- enables encrypted anonymous user access if desired
	- inefficient
	- `git clone https://gitserver/repos/sample_project.git`
- #### git protocol (server daemon)
	- most efficient data transfer
	- no auth support
	- requires additional config
	- does not encrypt traffic
	- commonly used for public access repo
	- `git clone git://gitserver/repos/sample_project.git`

## Configure Git for SSH access
- multi-user
- single-user
- most SaaS git providers use single user

### Configuring SSH access
- git hosting must reside within corpo data center
- traffic between client and server must be encrypted
- user authenticate to access remote repos
- it admin needs fine-grained access on user access even within repos

#### Configure client and server
- important steps i might forget (CLIENT)
	- create a specific user account for user (may be skipped)
	- `git config --global user.name "name", user.email "email"`
	- `mkdir ~/.ssh` if not yet existing, then `chmod 700 .ssh`
	- `ssh-keygen`
- recreate steps for server except ssh-keygen
	- add user public key to `~/.ssh/authorized_keys`
	- `chmod 600 authorized_keys
- now user can clone git repo hosted on client
	- provided that SSH access is enabled from firewalld
	- `git clone SERVER_IP:/path/to/repo.git`
#### User management
- append `git-shell` to `/etc/shells`
- change default server shell to git shell


# Git Actions CI
## Shell Commands vs Actions