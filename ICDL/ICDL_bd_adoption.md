# Big Data Adoption 
- challenges with storage and analysis
- identify behavior patterns to provide insights
- companies need this 
- GDPR
- important considerations for organizations
	- where can data be found?
	- goals of the analysis?
	- what value does it add? 
```toc
```

## Investment Requirement in BD Storage and Analysis
- ![[Pasted image 20230630122109.png|575]]
- implementation of big data requires investment. Solutions need to be purchased and experts need to be hired (for dumb managers)

### Storage and Networking
- first step is to store data in secure loc
- fast network = better multitasking / overall performance
- #### Hyperscale computing environments
	- storage techniques for big data
	- FAANG and IBM uses hyper-scale computing envs with
		- dedicated servers, attached storage, processing frameworks like hadoop.
		- include flash drives to reduce time taken to store or retrieve data  and improve performance
	- smaller organizations can use Network Attached Storage (NAS)
- #### Cloud Servers
	- latency, but very useful as backup
	- can be more expensive than other methods
	- more flexible (scale up or down as required)

### Processing
- **Splunk** offers cloud processing systems that are best for companies that experience seasonal peaks
- By 2025, data center energy consumption could use $\frac{1}{5}$ of global electricity.

### Analytics Software
- examine data and create useful info based on analysis
- factors
	- ease of use
	- security
	- type of analysis needed
- #### Descriptive Analytics
	- big data split into chunks
	- data aggregation and data mining give summary of findings
	- show underlying meaning in data (if any)
	- can be used in targeted ads (marketing)
		- historical data of consumers
		- analyze behavior and engagements
	- MS Excel, MATLAB, IBM SPSS (tools)
- #### Diagnostic Analytics
	- determine why something happened
		- root cause of event
		- what factors impacted which outcomes
	- help understand why sales have fallen in a time period
	- **attribute importance, sensitivity analysis, principal components analysis**
- #### Predictive Analytics
	- analyze soc med opinions on product X, predict whether reception of product is positive or negative
	- Sentiment Analysis?
	- Python, RapidMiner, IBM SPSS
- #### Prescriptive Analytics
	- given outcome X, suggest multiple courses of action
	- taxi service could analyze customer distance to nearby drivers
		- make suggestions on quickest option
- #### Employees
	- skills on data analysis tools
		- excel
		- power BI
		- SQL
		- R
		- Python
	- specialized competencies
		- AI
		- NLP
		- IoT
	- dedicated staff with skills = good investment

## Challenges to BDA
- unstructured data is challenging (according to lecture)
	- prolly because it is hard to define the right technique to analyze these (if you are a dumb management person)

### Challenges
- #### Data Quality
	- affected by data [[ICDL_ee_bigdata#Veracity||Veracity]]
	- inconsistencies in data quality
	- may vary wildly due to different sources
	- social media search history, watch history, machine data, tweets, IoT devices
	- while it is better to collect from multiple sources, it is more complicated
- #### Consistency
	- affected by [[ICDL_ee_bigdata#Velocity||Velocity]] and [[ICDL_ee_bigdata#Variety||Variety]]
	- slow analysis makes organizations miss out on opportunities
	- unstructured and semi makes analysis more complex and time-consuming
	- managing variety is important to conserve consistency
- #### System Compatibility
	- Challenge of making old data compatible with newer technology
- #### Synchronization
	- make data available on analytical platforms through synch
	- easy on paper, difficult to implement
- #### Skill Issue (Gaps)
	- need the right professionals to do the job (because you are a dumb manager)
## Big Data as a Service (DaaS) / Selling Analysis
- when facebook sells your data to third parties :(

#### Behavioral data insights
- targeted ads
- insight into user interest, likes, dislikes
- useful for corpos to alter products (or even reality) to satisfy customers

### BDaaS
- Facebook sells your data!
	- age
	- gender
	- current loc
	- email address
- targeted ads

### Insights from big data
- financial institution BBVA sells value-added analytics based on transaction data


## Ethical Considerations
- ethical / legal questions when organizations exploit data

### Good Governance
- private info needs to be protected (nobody does this)
- establish good governance structures (make sure you are following protocol!)
- goals of analysis should be articulated to avoid scope-creep, focus on goal
- authority needs to ensure that data is kept within goals
	- data is enough for analysis objectives
### Appropriate analysis
- meets agreed goals
- goals are ethical and legal
	- politics
	- race
	- religion
- ethical and legal basis for personal information

### Correct Analysis
- correct data and tools based on objective merit and valid outcome
- “How can an objective measure of product quality be derived from data”

### Legal Factors
- read up on the laws
- in countries where GDPR applies, sanctions are imposed on organizations that breach regulations


## Exploiting Big Data
- What are the goals of the analysis?
	- blueprint to set out why data analysis is being done in the first place
	- which areas will benefit?
- Where can the data be found?
	- internally or externally?
- How is the data structured?
	- may affect speed / consistency
- How can value be extracted from big data?
	- cleansing and extraction
	- tools / techniques to analyze data
- How can data be represented?
	- appropriate data visualization
	- Power BI or Tableau
	- bar / pie diagrams
- What continuous process improvement is required?
	- analysis should result in improvement of some business process


