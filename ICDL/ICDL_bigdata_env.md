# Big Data Environment
```toc
```

## What is Big Data Environment?
- data must be stored and accessed as needed
	- HDFS (Hadoop)
		- stores data in multiple computers connected to a network
	- Amazon S3
		- cloud-based storage
- Analyzed with Data analysis techniques
	- AB testing
		- split users between two versions of the website (feature being tested)
		- collect user behavior data 
		- evaluate which version is better (A or B)
	- Machine Learning
		- analyze data from past customers to predict room preferences

## Common Big Data Storage Technologies
- each day, 2.5 quintillion bytes of data is produced 
### Social Media Data
- most if not all actions on the internet are stored as data
	- tweets, search results, social media posts, etc.
- they are also analyzed to make targeted business decisions

### Big Data Storage as a Challenge
- since the [[ICDL_ee_bigdata#Volume||Volume]] is enormous, it is a challenge to store big data. 

### Distributed File System
- method of storing and accessing files stored in a server.
- one or more servers save the data, accessible by remote clients through auth
- large amounts of [[ICDL_ee_bigdata#Unstructured Data||unstructured data]] can be stored.
- Hadoop is an example of a distributed file system