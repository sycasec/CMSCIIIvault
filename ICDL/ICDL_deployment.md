# Cloud Deployment Models
```toc
```

## Introduction
### Customization and packaging
- users of any service should be able to pay only for what they use
- service must be customized for customer needs
	- banks have custom service based on client profile etc

## Features of private cloud models
### Definition
- cloud is owned by one specific company
- also known as internal or corpo cloud model
- #### On-site private cloud
	- implemented on a customer’s premises
- #### outsourced private cloud
	- server-side is outsourced to a hosting company or third-party vendor
- #### high security requirements
	- private cloud best for organizations with high security & management reqs
- #### Examples
	- Amazon Virtual Private Cloud (VPC)
	- Microsoft Azure Stack
- #### PROS
	- ##### High Security and privacy
		- maintained by cloud owner
		- firewall protection
		- user auth
	- ##### flexible
		- storage and network highly customizable
		- more flexible than other deployment models
	- ##### HIGH RELIABILITY
		- virtual operating environment
		- protects data from server/storage failure
- #### CONS
	- ##### COSTLY
		- designed to operate within an organization
		- more features, highly secure
		- cannot scale
	- ##### POOR SCALABILITY
		- **private cloud**
		- matches internal resources

## Features of public cloud models
- available to public 
- hosted by large tech providers
- resource sharing via internet
- server infrastructure maintained by vendors
- business can access services for free or pay-per-use
### EXAMPLES
-  google app engine
- microsoft azure
- amazon EC2
 
### PROS
- #### flexible
	- location independent
	- available anywhere anytime
- #### cost-effective
	- some are free, some are payperuse
	- infrastructure and maintenance performed by vendor
- #### scalable
	- resources can be generally used without limitation
	- you can be rate limited tho
### CONS
- #### Less data security and privacy
	- operated by third party
- #### Less reliable
	- operated by third party
	- storage / server unit failure, you can lose resources
- #### lack of individual approach
	- public cloud designed for general use
	- unsuitable custom approach 

## Community Cloud
- similar to private cloud
- services shared amongst organizations
- suited for organizations working on the same project
- #### Examples
	- AWS GovCloud
		- for US gov
	- SCC plc
		- sentinel community cloud solution
		- government level secure cloud services
		- framework developed by UK gov
### Pros
#### Cost reduction
- resources shared by organizations
- reduce cost
#### Better security, reliability, privacy
- operated by third party trusted by users
- members can access services and resources
- improves security of data stored
- less chance of server failure
#### Ease of data sharing and collaboration
- facilitates company collab
- easy to share resources assuming orgs have same requirements
### Cons
#### Higher cost
- designed for organizations with specific reqs
#### Scalability
- not scalable, only for fixed resources specified for sharing organizations
## Hybrid Cloud
- best features of private and public
- carry out non-critical tasks in public
- sensitive tasks in private
### Pros
- #### Improved security and privacy
	- use private and public
- #### enhanced scalability and flexiblity
- #### reasonable price
	- more expensive than public cloud
- #### Cloud bursting
	- app runs in private
	- bursts in public when demand increases
	- vendors handle traffic switching
		- non-sensitive functions into public servers
### Cons
- #### complex networking
- #### security compliance
- #### data splitting
	- can only be used if business splits data by level of sensitivity
