# Infrastructure as a Service (IaaS)

```toc
```

## Intro vid
- IaaS (basically Amazon)
	- you pay for the services you get
	- you can scale up on demand
		- you pay more if you scale up, less if down
- frees the business from the responsibility of managing own hardware
- 3rd party vendor manages all the IT stuff
- Business manages the setup of the apps and the computers


## Components of IaaS
- virtualized hardware
- virtualized environment
- load balancers
- cloud servers
- user controls allocated infrastructure through virtual env
- load balancers distribute traffic across servers
- ![[Pasted image 20230702123029.png|450]]

## Common Examples of IaaS solutions

### Amazon Web Services (AWS) EC2
- compatible with Windows and Linux
- NoSQL, relational db, Big Data
- scalable compute capacity
- develop and deploy faster

### Microsoft Azure
- SaaS and IaaS
- Microsoft-managed Data centers
- structuring, testing, deploying, monitoring (services and apps)
- appeal mainly to apps developed for windows
	- also supports linux

### Google Cloud Platform (GCP) - Google Compute Engine
- temporary storage and permanent disks
- load balancing, extended support for OS, live migration, faster persistent disks

### Alibaba
- growing (lmao, it is China’s Amazon tho.)
- investing heavily into global tech research facilities across China, Russia, Singapore, Israel, and U.S
	- Jack Ma still missing tho :((

### Rackspace
- ???
- American CC company
- platform offering website building, storage, access to virtualized servers
- preferred by companies with traffic fluctuations as they can remove cloud servers anytime

### Why would a business need IaaS?
- #### High performance computation
	- simulation, forecasting, decision making requires high performance computing
	- financial modeling, evaluating product design, forecasting weather (??), earthquake sim (??????)
	- IaaS is needed in such cases (not really IMO, more like you just need some experts. much cheaper)
- #### Data Analytics
	- anlayze huge amounts of data
	- marketing campaigns
	- big data analysis
- #### Hosting Complex Websites
	- online shop
	- ties in with data analytics
- #### Software Dev
	- quickly work on development and test environments
		- more like deployment / production hosting
- #### Multiple Web App support
	- hosting multiple web apps? ties in with software dev
- #### Complex storage and backup
	- what the fuck?
	- i am convinced the guy is just trying to reach 6 examples
	- why would you store backups in CLOUD???
	- anyway


## Benefits of IaaS

- **Anytime, Anywhere**
	- if you have internet connection
- **Greater Reliability**
	- you know what happened when amazon servers went down?
	- your DDOS problems are (virtually) solved
		- if amazon gets ddosed, you can sue amazon.
- **Pay Per Use**
	- on demand, business pays for resource actually used
		- the shadowy hand of jeff bezos adds invisible spending to your account
- **Scalability and Flexibility**
	- available to users when you need them (if they have internet)
	- scale up and scale down anytime
	- minimize wastage in capacity
- **Save time and effort**
	- you get to pay no experts to set up your network
- **Focus on core**
	- focus on business growth (good for small businesses)
- **Competitive edge**
	- because of all of the above, you get competitive edge

## Limitations of IaaS
- **Lack of Flexibility (???)**
	- actually means lack of control over what IaaS vendor manages
	- if you need the hardware to support X feature and vendor doesn’t work on it, you have a problem
- **Security and Privacy**
	- actually not a problem
	- you just need to read the vendor contract properly
	- if laws are breached, find ways to sue vendor
- **Technical Issues**
	- same as lack of flexibilty (lmao)
 - **Data dependency**
	 - ??? no proper explanation
	 - business depends on provider for data(??)