---
date_created: 2024-01-23
course: IBM_dataEng_ETLKafka
week: "4"
---
# Apache Kafka for Streaming Data Pipelines
```toc
```

## Distributed Event Streaming Platform (ESP) Components
### Event
- describe an entity’s observable state updates over time
	- GPS of a car
	- temp of a room
	- BP of a patient
- Common formats
	- plain text
	- hashmap
	- timestamp
### Event Streaming
- event source streams data to destination
- continuous streaming of data
- in real world, many to many relationship between source and destination
	- destination can also be a source (pipeline)
### ESP
- middle layer, unified interface ETL
- sources send to ESP
- destinations receive from ESP

### Components of ESP
- **Event Broker**
	- receive and consume events
	- three subcomponents:
		- *ingester*:  efficiently recieve events from various sources
		- *processor*: process events
		- *consumption*: retrieve events from storage and distribute to destination
- **Event Storage**
	- stored events, can be retrieved at will
- **Analytic and Query engine**
### Popular ESPs
- Amazon Kinesis
- Apache 
	- *Kafka* - most popular
	- Flink
	- Spark
	- Storm
## Apache Kafka Overview
### Use Cases
- track user activities
	- mouse clicks, keyboard clicks
- metric streaming
	- GPS, hw sw monitoring,
	- logs
	- payments and transactions
- database integration
- analytics
- notifications via email
- governance and audit
### Architecture
- distributed servers called brokers
	- managed by *Apache Zookeeper*
- TCP between clients and sservers
- Clients connect via Kafka CLI
### Main features
- distro system (???)
- highly scalable and reliable ??? 🤨🤨
- open source
### Corpos mooching off kafka
- Confluent Cloud (IBM? 🤨)
- IBM event streams 🤨🤨🤨🤨
- Amazon MSK (lmao 🤨🤨)
## Building Event Streaming Pipelines using Kafka
### Broker and topic
- brokers have topics
	- database that stores events
	- distribute events to consumers
- brokers replicate topics in different brokers  
### Kafka Topic CLI
- Create a topic
	- `kafka-topics --bootstrap-server localhost:9092 --topic log_topic --create --partitions 2 --replication-factor 2`
- List topics
	- `kafka-topics --bootstrap-server localhost:9092 --list`
- Get topic details
	- `kafka-topics --bootstrap-server localhost:9092 --describe log_topic`
- Delete a topic
	- `kafka-topics --bootstrap-server localhost:9092 --topic log_topic delete`
### Kafka producer
- client app that publish event to topic partitio
	- event can be optionally associated with a key
		- events with same key will be in same partition
		- unassociated events published to topic partitions in rotation 
- CLI
	- start producer to a topic
### Kafka Consumer
- clients subscribed to topics
- consume data in same order
- store an offset record for each partition
- playback possible
- producers dont need to synch with consumers                                                               

## Kafka Streaming Process
### Ad hoc weather stream processing 
- ![[Pasted image 20240125174418.png|675]]
### Kafka Streams API
- simple client lib to facilitate data processing in event streaming pipelines
- processes and analyzes data stored in kafka topics
- record only processed once
- process one record at a time 
- ![[Pasted image 20240125183433.png|600]]
- 