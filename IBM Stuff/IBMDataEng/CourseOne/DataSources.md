[[CourseOneRoot]]
# Sources of Data
```toc
```


## Relational Databases
- applications to support daily management of :
	- business activities
	- customer transactions
	- human resource activities
	- workflows
- these apps use RDBMS
	- sql server | oracale | mysql | ibm(??) db2
	- data stored in dbs are structured and can be leveraged for analysis
	- data from sale can be used to analyze sales patterns in diff regions
	- data from customer relationship management system can make sales projections

## Flat files and XML Datasets
- external to the org are public and private datasets
- gov orgs releasing demographic / economic datasets
- companies that sell data (oh my god)
	- point of sale data
	- financial data
	- weather data (oh okay)
- businesses can leverage these to:
	- define strategies
	- predict demand (oh my god)
	- make distribution decisions
	- make marketing promotions (oh my god)
- these datasets are given out as *Flat Files*, *Spreadsheet Files* or *XML docs*
- **Flat files**
	- store data in plain text
	- each line or row is one record
	- delimiter separated values 
	- maps to a single table
	- .CSV or .TSV
- **Spreadsheet files**
	- similar to flatfiles
	- organize data in tabular format
	- can contain worksheets that map to different tables
	- can be stored in custom formats and include additional information (formatting, formulas)
	- .XLS or .XLSX, Google Sheets, Appl numbers and LibreOffice (lmaoooo linux users)
- **XML Files**
	- values marked up using tags
	- complex data structures
	- data from online surveys | bank statements | unstructured data sets

## APIs and Web Services
- multiple users can interact with and request data for analysis
- listen for web requests from users or network requests from apps (or bots)
- return data in html / xml / json / media file
- Examples:
	- Twitter / Facebook API - customer sentiment analysis
	- Stock Market API for trading data - trading analysis
	- Data lookup and validation APIs - cleaning and co-relating data
	- Data from Database sources - website APIs in general

## Web Scraping
- extract relevant data from unstructured sources
- also known as screen scraping | web harvesting | web data extraction
- downloads specific data based on defined parameters
- can extract text, contact info, images, videos, product items, etc.
- **popular uses**
	- providing price comparisons by collecting product detail
	- generating sales leads through public data sources
	- extracting data from posts and authors on various forums (reddit)
	- collecting training and testing datasets for machine learning models
- **popular tools**
	- BeautifulSoup
	- ScraPy
	- Pandas
	- Selenium

## Data Streams and Feeds
- used for aggregating streams of data from:
	- instruments
	- IoT devices
	- apps
	- GPS data from cars
	- computer programs 
	- websites
	- social media
	- these data are timestamped geotagged (bro.....)
- **used for**
	- stock and market tickers for financial trading
	- retail transaction streams for predicting demand / supply chain management
	- surveillance and video feeds for threat detection (bruh......)
	- social media feeds for sentiment analysis (bro.....)
	- sensor data feeds for monitoring industrial equipment 
	- web click feeds for monitoring web performance and improving design (vine boom soudn fx)
	- real-time flight events for rebooking and rescheduling
- **apps used for this**
	- apache kafka
	- apache spark
	- apache storm
- **RSS (Really Simple Syndication) feeds**
	- capturing updated data from online forums and new sites like:
		- 