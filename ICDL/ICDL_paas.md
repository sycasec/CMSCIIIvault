# Platform as a Software (PaaS)

- vendor provides clients with a platform to create, run, and operate enterprise apps
- no building / maintenance of infrastructure (OS)
- AWS, Google, and most likely azure also provides PaaS
- Appfrog and Engine Yard (Only PaaS)

## Introduction
- third party provides hardware and software, typically those used for app development
- allows customer full control over the platform and the product
- **IaaS vs PaaS**
	- PaaS - vendor takes care of Servers, Networking, Sysadmin, setup the VM and RDBM + dev tools
	- IaaS only provides servers, networking, and sysadmin → VM setup and tools are left to the business
- **Infrastructure ++**
	- probably like firebase or something

### PaaS is designed to support the complete webapp lifecycle
- can be delivered as a:
	- public cloud service from a provider via internet
	- private service behind firewall, managed by an org’s IT department
	- Hybrid PaaS = private_cloud + n(public_cloud)

## Components of PaaS
### Databases
- RDBM tools
- Example
	- Azure SQL DB
### Web Servers
- managed and maintained by vendor
- Example
	- JBoss
	- Jetty
	- Tomcat
### Middleware
- webservers
- app servers
- content management systems
- tools that support app development and delivery
### OS
- you know what it is
### Dev Tools
- code editors / debuggers / compilers
- probably docker these days

## Examples of PaaS Solution Platforms
### AWS Elastic Beanstalk
- AWS
- quicker deployment
- business share services across devices
	- high scalability and security
- business focus on developing apps
### Google App Engine
- CC platform
- apps are run across multiple servers
- automatic scaling for webapps
- devs only code, no infrastructure maintenance / sysadmin
- free up to usage limit, more = paywall
### Microsoft Azure
- IaaS, PaaS, SaaS
- analytics, storage, networking, virtual computing
- flexible, open-source, reliable (??)
- pay-per-use
### Others
- Heroku
- Force.com
- Apache stratos
### Scenarios
- **DBMS** 
	- user can build their own db, dbms already set up
- **webapp hosting**
- **Big data**
	- storage and analysis

## Benefits
#### Supports multiple platforms
#### Cost Saving
- highly scalable, pay-per-use, etc etc
#### Guaranteed Updating
- vendor takes care of sysadmin
#### Quick app dev
- you only care about developing / hosting app on cloud
## Limitations
#### Dependency
- you need to trust that your vendor is competent (or sue them)
#### Vendor lock-in
- you are locked in to the setup provided by your vendor
#### Compatibility issues
- ties in with vendor lock-in, maybe difficult if attempting to migrate existing app to PaaS
#### Security Risks
- depends on your vendor, but most likely it is open source
