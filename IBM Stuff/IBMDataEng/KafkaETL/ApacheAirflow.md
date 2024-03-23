---
course: IBM_dataEng_ETLKafka
date_created: 2024-01-21
week: "3"
---
# Apache Airflow 
## Intro
- Apache airflow is an open source workflow orchestration tool
- build and run workflows drag and drop no code
	- workflow shown as directed acyclic graph
- not a data streaming solution
- ![[Pasted image 20240121123907.png|625]]
- ![[Pasted image 20240121123929.png|650]]
- ![[Pasted image 20240121124001.png|625]]
### Features
- Pure Python
- Useful UI with insights
- integration with other platforms
- unlimited pipeline scope
- open source
### Principles
- Scalable and Modular
- Dynamic Pipeline Generation in Python
- Extensible 
	- create your own operators and extend libraries
- Lean
	- jinja templating engine
### Use cases
- **sift** 
	- machine learning pipeline dependencies
- **seniorlink**
	- improve batch processes
- **experity**
	- deploy airflow as enterprise scheduling tool
- **onefootball**
	- orchestrate sql transformation in data warehouses
	- send daily analytics emails

## DAGs in Airflow
- represent workflows
- defined as code
- scheduled
- tasks are written in python, implementing operators
	- **Operators** determine what each *task* (node) does
		- *Sensor* operators poll for a certain time or condition
		- *Email and HTTP* operators
	- sample Python script block of DAG definition
	```python
	from airflow import DAG
	from airflow.operators.bash_operator import BashOperator
	import datetime as dt
	
	default_args = {
		'owner': 'me',
		'start_date': dt.datetime(now),
		'retries': 1,
		'retry_delay': dt.timedelta(minutes=5)
	}

	dag = DAG('example', description='example DAG', default_args=default_args, schedule_interval=dt.timedelta(seconds=5))
	```
### Airflow Scheduler
- persistent service in your environment
	- deploys on worker array
	- follows your DAG
	- first DAG run scheduled
	- trigger subsequent runs according to schedule
### Advantages of workflows as code
- Maintainable
- Versionable
- Collaborative
- Testable (??) 🤨

## Airflow Logging and Monitoring
### Logging
- saved to local .log files
- can also be sent to cloud storage
	- recommended to use elastic and splunk 🤨
- organized by dag and task IDs
### Monitoring Metrics
- **Counters** → metrics that always increase
	- total count of task instances failures 
	- total count of task instances successes
- **Gauges** → Metrics that may fluctuate 
	- Number of running tasks
	- number of dags in production
- **Timers** → time duration
	- ms to finish a task
	- ms to reach a success or failed state
### Storing and analyzing metrics
![[Pasted image 20240121193328.png|575]]