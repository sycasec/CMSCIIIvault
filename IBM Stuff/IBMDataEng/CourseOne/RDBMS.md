[[CourseOneRoot]]

# wk2-2

## RDBMS

- a relational database is a collection of data organized into a table structure, where the tables can be linked or related based on data common to each

### Used for:
- **Online Transaction Processing OLTP App**
- transaction oriented tasks that run at high rates and accomodate large numbers of users
- manage small amounts of data
- suppor frequent queries and fast response times


## NOSQL
- Key-Value store
	- data in a key-value db is key value pairs
- examples
	- redis
	- memcached
	- dynamoDB


## Data Wh, Marts, Lakes

### Data Warehouses
- has a 3-tier architecture
	- client frontend layer (query, report, analyze data)
	- OLAP server (process and analyze info coming from db)
	- DB servers
- benefits of cloud-based dwh
	- lower cost
	- limitless storage/compute cap
	- scale on a pay-as-you-go
	- faster disaster discovery
- examples:
	- teradata
	- oracle exadata
	- ibm db2
	- netezza
	- amazon redshift
	- google bigquery
	- cloudera
	- snowflake

### DM
- built for a specific use
- provide data to users most relevant to them on demand
- accelerate business processes
- provide cost and time efficient way to make data driven decisions
- Dependent
	- analyitcal caps of a restricted area of the dwh
- Independent
	- created from sources other than an enterprise dwh
- Hybrid
	- combine inputs from dwh, operational systems and external systems


### DL
- large amounts of struct, semi-struct, unstruct data in their native format
- dat can be loaded without defining the structure and schema of data
- repo of raw data straight from source
- classified, protected and governed
- reference architecture combining multiple techs
- can be deployed using
	- cloud object storage (amazon s3)
	- apache-hadoop
	- rdbms/nosql
- **Benefits**:
	- store all types of data
	- scake base on storage cap
	- saving time in defining structs, schemas and transformations
	- repurpose data in several dif ways



## etl, elt, pipes

### ETL
- gather raw data
- extract info needed
- clean, standarize, transform data
- load int o repo

#### Extracting
- scraping
- stream procecssing
- batch processing

#### Transform
- standardize date formats
- remove duplicate data
- etc just clean the data as needed

#### Load 
- up to repo


### ELT
- advantages:
	- shorten cycle between extract and delivery
	- ingest raw data immediately
	- greater flexibility for analysts / ds
	- transform data on demand
	- more suited to big data


### Pipes
- journey of data from one system to another
- batch and streaming data
- long running batch and small interactive q
- load data into DL or any destination
- examples:
	- beam
	- airflow
	- dataflow


## Data Integration
- **tools**:
	- ibm infosphere info server
	- cloud pak for data
	- cloud pak for integration
	- data replication
	- data virtualization manager
	- infosphere information server on cloud
	- infosphere datastage