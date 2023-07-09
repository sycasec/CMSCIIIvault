# Cloud Computing
- anything related to the internet
```toc
```

## Cloud Computing Def
- in business, actually means outsourcing hosting responsibilities to 3rd party vendors (Amazon, Azure, Google, etc.)
- data storage, compute power, without having the applications / tools / tech locally

## Characteristics

### Wide Network
- use can access and upload data from anywhere anytime (given internet connection + device)

### Pay Per Use
- user pays for utilized service

### Flexible 
- resources can be scaled up or down rapidly

### Resource Pooling
- users share the same physical runtime behind the scenes
- retain privacy and security


## Origins of CC

### Time sharing (Early 1960s)
- time sharing / multiprogramming (by John McCarty apparently)

### Client-Server Model (1964) 
- workloads are partitioned between servers and clients
- example is email, network printing, www
	- a server exists to serve the service
	- a client uses (requests) the services

### Intergalactic Computer Network (1969)
- J.C.R Licklider
- enabled the development of ARPANET (Advanced Research Projects Agency Network)

### Virtualization (1970)
- VMwar, run a completely different computer (VM) inside an existing OS
- took time sharing model to the next level

### First known definition of CC (1997)
- Ramnath Chellappa of Emory Uni and Uni of Southern California defined CC as
	- “A computing paradigm where the boundaries of computing will be determined by economic 
	  rationale rather than technical limits alone”

### Salesforce.com (1999) 
- concept of delivering enterprise applications via the web

### AWS (2002)
- Amazon Web Services providing cloud services
	- storage
	- computation

### Amazon Cloud Services expansion (2006)
- Elastic Compute Cloud (EC2)
- allowed people to access computers and run their own apps
- Simple Storage Service (S3) pay-as-you-go model

### Entry of Google and Microsoft (2009)
- Google Apps bought cheaper computing and storage services
- Microsoft launched azure

### \$100 B (2013)
- 30 large companies collectively represent more than \$100 B in market capitalization
- CC industry came of age with IaaS (infrastructure as a service)

### \$258 B (2019)
- rapid growth
- 90% of companies are in the cloud
- AWS is the leading cloud vendor with a 32% market share
- market expected to reach \$623.3 billion by 2023
- Nort America and Europe together dominate the global cloud computing market

## Cloud Computing Key Services: IaaS, PaaS, SaaS

![[Pasted image 20230702121859.png|700]]

### SaaS
- delivers apps over the internet through browser
- no downloads / installs (web pages)
- CSP installs, operates, maintains software apps
- Example: Office 365
	- actually is a web based app
	- runs in the browser, but you can download the shit as well

### PaaS
- Platform for software creation
- alot like IaaS, except you just deploy the App and manage Data
- runtime, middleware, OS is maintained by the vendor
- example: 
	- Google App Engine


### IaaS
- vendor handles the servers, storage, networking, and virtualization
- business retains control over apps, runtime, middleware, and OS


![[Pasted image 20230702122410.png|600]]

### FaaS
- serverless architecture
- devs just write code lmao
- that’s weird
- maybe this is for the running your ML algo and stuff