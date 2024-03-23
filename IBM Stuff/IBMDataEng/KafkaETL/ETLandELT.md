---
course: IBM_dataEng_ETLKafka
date_created: 2024-01-19
week: "1"
---
# Kafka ETL & ELT
```toc
```

## Course Introduction
- ETL stands for **Extract**, **Transform**, **Load**
- ELT is similar but loads the data in raw format, reserving transformations for later in “self-serve analytics”

## ETL Fundamentals
- ETL
	- extract 
	- transform
	- load
- curating data from multiple sources
- format and load
### What is Extraction?
- get access and read into application
- examples:
	- web scraping
	- API
- may be static or streaming
### Transformation
- also known as wrangling
- conform to target system and use cases
- processes:
	- cleaning
	- filtering
	- joining / merging
	- feature engineering
	- formatting and data typing
### Loading
- move data into new environment
- usually among the following:
	- warehouses
	- mart
	- database
- can also mean preparing data for end user

### Use Cases
- Digitizing analog media
- moving data from  OLTP to OLAP systems
- creating dashboards
- machine learning

## ELT vs ETL
- **ETL**
	- etl is for a fixed function
- **ELT**
	- elt is for where users want the raw data, the data is what the users want
	- created to get access to data rather than waiting for business mandated analytics
- trend of shifting from ETL → ELT
	- waiting for analytics made by data source is tiresome
	- users want to customize their own dashboard
	- users want to do other things with the data

## Data Extraction Techniques
- *Raw Data Sources*
	- documents
	- web pages
	- analog audio video
	- survey, stats, economics
	- transactional data
	- social media 
	- weather station
	- IoT
	- medical records
	- human genome
- **Techniques for extraction**
	- *Optical Character Recognition* (OCR) - used to digitize text
	- ADC (analog to digital converters) sampling→ digitize audio / video recordings 
	- Cookies, user log
	- web scraping
	- API (reddit, twitter)
	- database query
	- edge computing (traffic data from video cams)
## Data Transformation Techniques
- format data to suit application
	- data typing (changing to appropriate types)
	- data structuring
	- anonymizing
	- cleaning
	- normalizing
	- filtering, sorting, aggregating, binning
	- joining / merging data sources
- *Schema on write*
	- conventional ETL approach
	- data is conformed to schema before loaded
- *Schema on read*
	- schema is applied to data after reading from raw storage
	- most likely you apply the schema yourself
- *Data Loss in Transformation*
	- lossy data compression
	- filtering
	- aggregation
## Data Loading Techniques
- Techniques
	- Full
		- load everytthing
	- Incremental
		- appended
	- Scheduled
		- periodic loading
	- On-demand
		- loaded when requested
- *Batch loading*
	- periodic updates using windows of data 
	- hours to days
- *Stream Loading*
	- loads data in real time
- *Push and pull*
	- Pull
		- request data from client
	- Push
		- send data to server