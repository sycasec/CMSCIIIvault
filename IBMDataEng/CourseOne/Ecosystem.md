[[CourseOneRoot]]
# Data Engineering Ecosystem
```toc
```

## Includes:
- Infrastructure, tools, frameworks, and processes for:
	- Extracting data from disparate sources
	- Architecting and managing data pipelines for transformation, integration, and storage of data
	- Architecting and managing data repos
	- Automating and optimizing workflows and flow of data between systems
	- Developing application needed through the data engineering workflow

## Data
- **Structured**
	- Follows a rigid format and can be organized into rows and columns
	- typically in db and spreadsheets
- **Semi-structured**
	- mix of data that has consistent characteristics and data that does not conform to a rigid structure
	- emails, reddit posts
- **Unstructured**
	- data that is complex and mostly qualitative information that cannot be structured into rows and columns
	- photos, videos, pdf files, social media content
- **Sources**
	- Relational Database
	- NoSQL DB
	- APIs
	- Web services
	- Data Streams
	- Social Platforms
	- Sensor Devices

## Data Repositories

### Transactional
- **Transactional** or **Online Transaction Processing (OLTP) System**
- High volume day to day data
	- banking transactions
	- atm transactions
	- airline bookings
- usually rdbm, sometimes no sql
### Analytical
- or **Online Analytical Processing (OLAP) System**
- optimized for conducting complex data analytics
	- relational and non relational db
	- data warehouses, marts, lakes
	- big data stores

## Data Integration
Data is:
- Collated -> Processed -> Cleansed -> Integrated -> Accessed by Users
- Data is combined into a unified source/view, accessed by users to query and manipulate the data

## Data Pipeline
set of tools and processes that cover the entire journey of data from source to destination
- Extract -> Transform -> Load (ETL) Process
- Extract -> Load -> Transform (ELT) Process

## Languages
- Query languages
	- SQL -> Query / Data manip
- Programming languages
	- Python -> Data apps
- Shell and scripting languages
	- automation

## Building Business Intelligence (BI) and Reporting Tools
- collect data from multiple sources and present them in visual format
	- dashboards, chats, reports, etc
- visualize data in real-time and pre-defined schedule
- drag and drop products that do not require knowledge of programming