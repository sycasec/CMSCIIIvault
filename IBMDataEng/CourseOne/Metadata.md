[[CourseOneRoot]]
# Metadata

```toc
```

## Technical Metadata
Technical metadata is metadata which defines the data structures in data repositories or platforms, primarily from a technical perspective.

For example, technical metadata in a data warehouse includes assets such as:
-   Tables that record information about the tables stored in a database, like:
    -   each table’s name
    -   the number of columns and rows each table has
-   A data catalog, which is an inventory of tables that contain information, like:
    -   the name of each database in the enterprise data warehouse
    -   the name of each column present in each database
    -   the names of every table that each column is contained in
    -   the type of data that each column contain

The technical metadata for relational databases is typically stored in specialized tables in the database called the System Catalog.

## Process Metadata
- Process metadata describes the processes that operate behind business systems such as data warehouses, accounting systems, or customer relationship management tools.

- Many important enterprise systems are responsible for collecting and processing data from various sources. Such critical systems need to be monitored for failures and any performance anomalies that arise. Process metadata for such systems includes tracking things like:
	-   process start and end times
	-   disk usage
	-   where data was moved from and to, and
	-   how many users access the system at any given time
	- This sort of data is invaluable for troubleshooting and optimizing workflows and ad hoc queries.

## Business Metadata
- Users who want to explore and analyze data within and outside the enterprise are typically interested in _data discovery_. 
- They need to be able to find data which is meaningful and valuable to them and know where that data can be accessed from. 
- These business-minded users are thus interested in business metadata, which is information about the data described in readily interpretable ways, such as:
	-   how the data is acquired
	-   what the data is measuring or describing
	-   the connection between the data and other data sources
- Business metadata also serves as documentation for the entire data warehouse system.

## Why is Metadata important?
- Good metadata management has many valuable benefits. 
- Having access to a well implemented data catalog greatly enhances:
	- data discovery, repeatability, governance, and can also facilitate access to data.
- Well managed metadata helps you to understand both the business context associated with the enterprise data and the data lineage, which helps to improve data governance. 
	- Data lineage provides information about the origin of the data and how it gets transformed and moved, and thus it facilitates tracing of data errors back to their root cause. 
	- Data governance is a data management concept concerning the capability that enables an organization to
		- ensure that high data quality exists throughout the complete lifecycle of the data, 
		- and data controls are implemented that support business objectives.
- The key focus areas of data governance include 
	- availability, usability, consistency, data integrity and data security 
	- and includes establishing processes to ensure effective data management such as 
		- accountability for the adverse effects of poor data quality 
	- and ensuring that the data which an enterprise has can be used by the entire organization.

## Popular Tools for metadata Management
Popular metadata management tools include:
-   IBM InfoSphere Information Server
-   CA Erwin Data Modeler
-   Oracle Warehouse Builder
-   SAS Data Integration Server
-   Talend Data Fabric
-   Alation Data Catalog
-   SAP Information Steward
-   Microsoft Azure Data Catalog
-   IBM Watson Knowledge Catalog
-   Oracle Enterprise Metadata Management (OEMM)
-   Adaptive Metadata Manager
-   Unifi Data Catalog
-   data.world
-   Informatica Enterprise Data Catalog