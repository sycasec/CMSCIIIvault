[[CourseOneRoot]]

# Data Platofrms, Data Stores, Sec

```toc
```

## Designing Data Platforms

### Data Ingestion/Collection layer
**what it does**
- connect to data sources
- transfer data from data sources to data platform in streaming and batch modes
- maintain info about the data collected in metadata repo
**tools**
- google data flow
- ibm streams
- ibm streaming analytics on cloud
- amazon kinesis
- apache kafka
  
### Data storage & integration layer
 **what it does**
 - store data for processing and long term use
 - transform and merge extracted data
 - make data available for streaming and batch modes
 **needs to be**
 - reliable, high perfroming, scalable, cost-efficient
 **tools**
 - any sql/nosql db server ever
   
### Data processing layer
- applying data validation, transformation, and business logic to data
- read data in btach or streamign modes from storage and apply transformations
- support popular querying tools and prog lang
- scalable
- allow analysts to get data
**transformation tasks**
- structuring - change the form/schema of data
- normalization - data cleaning
- denormalization - combine all data into single table
- data cleaning - isnt this just normalization
**tools**
- spreadsheets or python or r idk 


### Analysis & user interface layer
- you already know

### data pipeline layer
- ETL tools
- you already know 



## Designing Data Stores
- data repo
- can be used for business ops / reporting & analytics
- can be db / warehouse / mart / big data store / data lake
- considerations for design

### Type of data
- RDBMS for structured data
- nosql db for unstructured / semi
	- key-value 
	- doc-based - not best for complex search queries
	- col-based 
	- graph-based - not good for large-volume analytics queries

### Volume of data
- data lake - for shitton raw data native format
- big data store - for high (volume, velocity ??) diverse types, fast analytics
	- stored in multiple computers

### intended use of data
- number of transactions
- freq of updates
- types of ops
- response time
- backup & recovery
**types of systems**
- transactional - high-volume, high-speed 
- analytical - complex queries - large amounts of historical data - faster response times

### storage considerations
- performance - throughput and latency
- availability - no downtime
- integrity - security lmao
- recoverability - just keep backups

### priv,sec,gov needs
- access control
- multizone encryption
- data management
- monitoring systems

**laws i guess**
- general data protection regulation (GDPR)
- cali consumer priv act (CCPA)
- health insurance portability and accountability act (HIPAA)


## Security
### CIA triad
- confidentiality - control unauth access
- integrity - validate resource
- availability - keep the db up for valid users

### physical infrastructure sec
- not really a data engineer's prob, more like an architect's problem.
- restrict perimeter access
- monitor entry/exit points
- dedicate powerfeeds/generators/ups battery backup for servers
- dedicate heating/cooling mechanisms for servers
- environmental threats (again, not the data eng's prob)

### network sec
- firewalls
- network access control
- network segmentation - vlan
- security protocols
- intrusion detection - so basically you keep sniffing packets and monitor your employees to *make sure* nobody attacks. hmmmm.

### app sec
- threat modeling
- secure design & coding (isn't this part of the same process)
- security testing

### data sec
- isnt this just netsec
- passwords, tokens, biometrics
- **data at rest**
	- non moving data (files, objects, etc)
	- stored in db, wh, tapes, backups, etc
	- encrypt
- **transit**
	- moving
	- encrypt with https,ssl,tls

### monitoring and intelligence
- monitor -> track -> react
- **security mon and int sys**
	- create audit history
	- provide reports & alerts