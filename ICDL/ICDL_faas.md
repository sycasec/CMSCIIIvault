# Serverless or FaaS
```toc
```

## Function as a Service
- IaaS reduced time and money needed for implementing and maintaining the physical resources required to keep important apps running
- PaaS provided technologies that allow clients to focus on development and business operations
- SaaS allowed simple access to an application / software via internet
	- no longer need to maintain, upgrade, or manage hardware / software
- **FaaS**
	- serverless computing
	- introduced in 2010, formally in 2014
	- still uses servers, developers do not have to monitor servers (hence serverless)

### FaaS vs PaaS
- FaaS is inbetween PaaS and SaaS i guess
- FaaS billing scales on demand

![[Pasted image 20230706084135.png|625]]


## Features and Purpose of Serverless Solutions

### Principal Feature
- #### Up when needed
	- brought up when needed (down when not used)
	- payment per request
- #### Access anytime
- #### Reduces development time
- #### Highly scalable
- #### Pay per request


### Common Examples
#### AWS Lambda
- first public cloud infrastructure
- introduced by amazon in 2014
- AWS handles all operations as well as maintenance of backend components
- **Netflix** uses lambda to help manage computing and storage infrastructure with event-based systems
	- triggered by events such as HTTP requests, new database entries, or message notifications

#### Google Cloud Functions
- used by google for google search, gmail, youtube

#### Azure Functions and IBM Cloud Functions


### Scenarios which FaaS fits best
#### High volume parallel workloads
- high scalability allows hits
- can also be used to create backend systems or data processing
#### Webapps, chatbots, IoT devices
#### App development
- charged only when apps connect to cloud for functions such as batch processing

