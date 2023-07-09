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
- simplified DFS architecture
- ![[Pasted image 20230630060553.png|325]]
- Two types of DFS
	- #### NAMESPACE
		- multiple DFS namespaces
		- different folder targets in different servers mapped to one share path
		- folders are stored in different databases
		- ![[Pasted image 20230630060805.png|400]]
	- #### REPLICATION
		- user creates a replication group
		- settings like scheduling, bandwidth throttling are configured by admin
		- no need to copy files manually
		- ![[Pasted image 20230630060932.png|367]]

## Cloud Storage
- relatively new method of storing data
- provides flexibility
	- for enterprises, this allows data control anywhere anytime
		- cheaper alternative to other storage methods
	- for end-users, it helps in backups of their data
		- allows for usage anywhere anytime
- major providers
	- Microsoft
	- Amazon
	- Google
	- Dell
	- HP
	- IBM
	- Rackspace
	- CISCO
- may raise security issues, but encryption is usually used for cloud servers

## Things to know
- the two most common ways for the storage are Hadoop Distributed File System and Amazon S3

### HDFS
- Apache Hadoop is FOSS
- uses network of computers to manage & process big data
- benefits:
	- speeds up data processing
	- prevents data loss
	- cost-effective method
	- highly scalable
	- requires little administration

### AMAZON S3
- Also called amazon simple storage service
- benefits:
	- cloud-based storage service
	- popular, used for website data, backups, IoT data, and data analysis
	- data security techniques such as encryption and management tools

### Key Differences
| Category     | [[#HDFS]]                                                                                                                                             | [[#AMAZON S3]]                                                                                                                                                                     |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Storage** Type | Physical Storage - not cost effective since upgrading requires new hard drives                                                                        | Charged every month per storage space used                                                                                                                                         |
| **Security**     | builtin security features like user authentication and file permissions, files are stored at multiple locations. backup is stored in one single drive | user authentication - bucket and object owners can access data. Next Step permission can be granted to users via bucket policies and Access Control Lists. More flexible than HDFS |
| **Performance**  | Stored on local drives, faster but speed depends on quality of local servers                                                                          | cloud storage, requires stable network and compatible devices                                                                                                                      |


## Common Approaches to Big Data Analysis
- increasingly being deployed in many organizations
- organizations want to gain insights to improve business processes
	- shopping recommendations (targeted ads, targeted recommendations, etc.)
	- done by data analysis of customer purchase / view / search history


### Big Data Analysis
- methods for examining large data sets to draw helpful conclusions and predictions (insights)
- allows companies to forecast/predict customer and competitor behavior, as well as daily performance of own workforce
- important where huge volume of observational data is gathered
	- astronomical data from satellites & telescopes
- data may be broad and unstructured
	- summarizing / gaining insights becomes challenging
	- data analysis techniques are used

### A/B testing
- a control group is compared with test group to determine a better feature (A or B)
- can improve marketing response 
- also known as bucket testing / split testing
- helpful for :
	- deciding UI/UX design / interface.
	- testing marketing or email ads
	- managing streams of real time data 
- #### General Steps
	- Choose what needs to be compared
	- decide what should be measured with the test
	- create an A/B test and add variants to it.
	- Select criteria for the A/B test. For example, start and end date.
	- View the results in an A/B test report.

### Data fusion and integration
- analysis of data from multiple sources
- more accurate than those derived from single source.
- allows a more complete understanding of users.
- Oracle’s GoldenGate products are tools for real -time data integration.

### Data Mining
- analysis technique for information extraction from big data.
- meaningful trends and patterns can be analyzed.
- Examples:
	- Spam filtering
	- credit risk management
	- database marketing
	- customer opinion analysis
	- fraud detection
- SAS enterprise miner is a solution for models based on big data from different sources (within org).
	- simplifies data preparation
	- helpful in creating models faster
	- costly for small businesses

### Machine Learning 
- make forecasts based on large datasets
- models can learn based on data provided
- Oracle’s Machine Learning product family is an enterprise software that analyzes business trends
	- used to 
		- process data where it is stored by using distributed algo
		- process data lakes that use hadoop and spark
		- use SQL and R 

### NLP 
- analyze corpus of text
- pattern recognition, automated response / translation, etc.
- can be used to summarize large documents
- SAS Visual Text Analytics uses NLP to examine unstructured data (text)
	- supports 33 languages with features like parsing, sentiment analysis, trend analysis

### Statistics
- you know what it is
- #### sampling
	- sample is taken from dataset
	- model estimates and forecasts from sample
- #### Divide and Conquer
	- dataset divided into small blocks that are easily analyzed
	- result for each block combined to provide a holistic analysis for whole.


## Big Data Visualization
- Big data enhances a company’s decision making capability
	- improve quality of service
	- efficiency
	- logistics
	- user preference
	- forecasting
	- **profit**
- visualization is necessary because management people are dumb
- dumb managers need visualization to help them make decisions (because they’re dumb)
- present data using crayons and easy words to make children (dumb managers) understand

### 2D Area
- that map chart thing where color / gradient represents something
- **area or distance cartograms**
	- that’s what they’re called

### Multidimensional
- Scatter plot (lmao)

### Hierarchical Data Viz
- **Dendrogram**
	- tree like diagram that shows hierarchical clustering between datasets
	- in medicine, it is useful for gene / sample clustering

### Network Data Models
- obsidian graph view!
- relationships between data elements or datasets
- **Node-link diagram**
	- a graph, they just had to rename it (dumb managers).

### Temporal Visualization
- Histogram
- start and finish time, descriptive image of a variable that changes over time
- **Polar Area diagram**