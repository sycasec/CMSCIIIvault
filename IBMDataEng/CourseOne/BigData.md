# Big Data
[[CourseOneRoot]]

```toc
```

## Foundations

> Big Data refers to the dynamic, large, and disparate volumes of data being 
> created by people, tools, and machines. It requires new, innovative and scalable
> technology to collect, host, and analytically process the vast amount of data
> gathered in order to derive real-time business insights that relate to consumers,
> risk, profit, performance, productivity management, and enhanced shareholder value

- 5 v's of data
	- velocity - speed in which data is gathered
	- volume - scale of the data
	- variety - diversity of the data
		- drivers: Mobile Tech | Social Media | IoT | Geo Tech | videos
	- veracity - origin of data and its facts and accuracy
	- value - benefit of data 

## Processing Tools 
- provide ways to work with large sets of struct/semi/unstruct data do derive value from data
- Apache Hadoop
	- collection of tools that provides distributed storage and processing of big data
	- Hadoop Distributed File System (HDFS) storage system running on  netowrk
		- provides scalable big data storage
		- replicates file blocks on different nodes
		- higher availability, better scalability, data locality
		- fast recovery from hardware failures
		- access to streaming data
		- accommodation of large data sets
		- portability
- Apache HIve
	- open source data warehouse software for rw and managing large data sets
	- high latency queries, slow response
	- read based
	- data warehousing tasks, etl, reporting
- Apache Spark
	- general-purpose data processing engine
	- used for:
		- interactive analytics
		- streams processing
		- ml
		- data integration
		- etl
	- in-memory processing
	- interfaces for java, scala py, r, sql
	- standalone clustering
		- or hadoop
	- access data from hdfs or hive
	- process streaming data fast
	- comples analytics in real time
- 