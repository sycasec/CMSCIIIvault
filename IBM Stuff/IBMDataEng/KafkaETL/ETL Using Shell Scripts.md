---
course: IBM_dataEng_ETLKafka
date_created: 2024-01-20
week: "2"
topic:
---

# ETL Using Shell Scripts
## ETL Techniques
- *Extract*
	- first step of the process
	- raw data from any source
- *Transform*
	- normally done in work environment called “**staging area**”
	- processes are applied to data to prepare for loading into target system
	- **transformations applied**
		- **cleaning**: fixing errors or missing values
		- **filtering**: filtering out unnecessary data
		- **joining**: merging “disparate” data sources
		- **normalizing**: converting data to common units (different currencies to a singular one like \$)
		- **data structuring**: converting one data format to another (XML → JSON)
		- **feature engineering**: creating KPIs for dashboards or machine learning
		- **anonymizing and encrypting**: ensure data privacy and security
		- **sorting**: ordering the data to improve search performance
		- **aggregating**: summarizing granular data
- *Load*
	- load data into target software / system 
### ETL workflows as Data Pipelines
- to boost data processing efficiency, data is fed through a *data pipeline*
	- while one packet is being extracted, an earlier packet is being transformed
	- ![[Pasted image 20240120184826.png|625]]
- with conventional ETL pipelines, data is processed in **batches**
	- usually on a repeating schedule that ranges from hours to days apart
	- for example, records accumulating in an Online Transaction Processing System (OLTP)
		- can be moved as a daily batch process to one or more Online Analytics Processing (OLAP) system
		- analysis of large volumes of historical data is carried out
	- **Batch processing** intervals can be triggered by events, such as:
		- source data reaches a certain size
		- an certain event occurs
		- on-demand processing, with web apps such as music or video streaming services
### Staging Areas
- ETL pipelines are used to integrate data from disparate and siloed systems within the enterprise
	- data from different vendors, locations, divisions, etc.
	- adds operational complexity
- ![[Pasted image 20240120185303.png|600]]
### ETL Workflows as DAGs
- Apache Airflow is used as an ETL workflow orchestration tool 
- *Popular ETL Tools*
	- there are many ETL tools available online, including features such as:
		- automated pipelines
		- easy to use with default rule recommendations
		- drag and drop, “no-code” processing for workflows
		- transformation support on complex calculations
		- security and compliance
	- *open source*
		- **Talend Open Studio**
			- Supports big data, data warehousing
			- collaboration, monitoring, scheduling
			- drag and drop for ETL pipeline workflow creation
			- JAVAAAAAAAA 🤨🤨🤨🤨🤨🤨🤨🤨🤨🤨🤨🤨🤨🤨🤨🤨🤨🤨
			- integrates with many data warehouses
			- open-source
		- **airflow**
			- versatile config as code data pipeline platform
			- open-sourced by airbnb
			- programmatically author, schedule, and monitor workflows
			- scales to big data
			- integrates with cloud platforms
		- **pandas**
			- versatile open-source programming tool
			- doesnt readily scale to big data ?
	- *Enterprise*
		- **AWS Glue**
			- simplifies data prep for analytics
			- auto suggest schemas for storing data
			- create ETL jobs from AWS console
		- **Panoply**
			- ELT specific platform 
			- no-code data integration
			- SQL-based view creation
			- shifts emphasis from data pipeline development to data analytics
			- integrates to tableau and powerBI
		- **IBM InfoSphere**
			- data integration tool for designing, developing, and running ELT and ETL jobs
			- data integration component of IBM InfoSphere and Info Server
			- drag and drop GUI
		- **alteryx**
			- self-service data analytics platform
			- dnd ETL tools
			- no sql for pipelines
		- **IBM Streams**
			- build real-time apps using SPL, Java, Python, or C++
			- combine data in motion (???) and at rest (???) to deliver real-time intelligence
			- end-to-end processing
## ETL using shell scripting 🤨
- sample task: report temperature stats for a remote location
	- hourly average, min, max temp
	- remote temp sensor
	- update every minute
- given:
	- `get_temp_api` → read temp from remote sensor
	- `load_stats_api` → load stats to dashboard repo  

## Data Pipelines
- series of connected processes
- mass production
- moves data from place to another, with optional stages
- includes low-level hardware architectures
- *performance*
	- latency
	- throughput
- *use cases*
	- back up files
	- integrate raw data source into data lake
	- moving transactional records to data warehouse
	- streaming data from IoT devices to dashboard
	- prepare data for machine learning
	- messaging systems
## Key Data Pipeline Processes
- *Extraction*
- *Ingestion*
- *Transformation*
- *Loading*
- *Scheduling*
- *Monitoring*
	- latency
	- throughput
	- warnings, errors failures
	- utilization rate
	- logging and alert system
- *Maintenance and Optimization*
### Load Balanced Pipelines
- JIT data packet relays
- no upstream data flow bottlenecks
- uniform packet throughput throughout all stages
- parallelize stages? 🤨🤨🤨
### Stage synchronization
- I/O buffers can help synchronize stages
- holding area for data between processing stages

## Batch vs Streaming Pipeline use cases
### Batch data pipelines
- operate on batch data
- usually run periodically  
- can be initiated based on certain triggers
- cases where recency of data are not necessary
- appropriate for when accuracy is critical
### Streaming data pipelines
- ingest packets in rapid succession
- minimal latency 
- records / events are processed as they happen
### Micro-batch data pipelines
- faster processing, simulate real-time streaming
- improve load balancing, lower latency
- short windows of data are required
### Batch vs Stream
- accuracy vs latency requirements
- data cleaning improves quality, but increases latency
- lowering latency induces errors
### Lambda architecture
- historical data batches → batch layer
- streaming data → speed layer
- data stream fills latency gap
- used when data window is needed but speed is also critical 
- high logical complexity
- **use cases**
	- *batch*
		- data backups
		- transaction / history loading
		- billing and order processing
		- data modelling
		- forecasting sales or weather
		- data analysis
	- *streaming*
		- movies
		- social media feeds
		- fraud detection
		- targeted ads
		- stock market
		- real-time product pricing

## Data pipeline tools and tech
- typical enterprise grade tech
	- automation → fully automated pipelines
	- ease of use → etl rule recommendations
	- drag-and-drop → no code rules and workflow
	- transformation support → assistance with complex calculations
	- security and compliance → data encryption
