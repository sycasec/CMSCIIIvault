# General Steps
## Creating the main system
### Controller / System Main
- generates (1-30) users
	- upon generation of users, system should allow users to know how many resources are available for use
	- user will randomly select from the available resources (1, n_resources)
		- with random time (1, MAX_TIME)
	- system’s list of users will be the basis of who is served resources first.
	- system will handle attachment of user to resources.
- generates (1-30) resources
- should keep track of timer
	- in extension, handle all other processes
### User
- 