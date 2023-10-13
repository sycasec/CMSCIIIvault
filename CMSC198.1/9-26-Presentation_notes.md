
```toc
```

chair
table
pluma

## What is short-term traffic forecasting
### Definition
- Bogaerts et al (LONG TERM TF) 2020
### Vlahogianni, Karlaftis & Golias
- **predictions made from few seconds to possibly few hours into the future based on current and past traffic information**
- most literature focused on methodologies for modeling traffic volume, density, speed, travel times, and produce anticipated traffic conditions
- STTF has been a very important consideration in many areas of transportation for more than 3 decades
- direct result ofi ncreasing need for developing apps that provide accurate info to drivers and for signal optimizaion
- ITS Technology and Analytical data analysis have been the focus of countless research papers, wherein increased data availability and processing speed brought great advances
- STTF has been an integral part of ITS related research
- moved from classical statistical (ARIMA type models) to neural and evolutionary computational approaches due to the rise of Computational Intelligence (CI) - Data Mining (DM) approaches to analyzing data.
#### HISTORY 
- started with [Ahmed and Cook, 1979](https://trid.trb.org/view/148123) 
- most research used classical statistical approaches
	- shown to be weak or inadequate under unstable traffic conditions, complex road settings, or extreme datasets (structured & unstructured)

#### REVIEW 
- most data come from motorways and freeways
- (mostly) univariate statistical models are used to analyze the data
- literature focused on predicting traffic volume || travel time
- predictions made based on single point sources

#### CHALLENGES
- developing STTF models that can account for weather changes, unexpected events (car crashes, construction work, etc.)
	- models have been developed to try and account for this but with no clear results
- existing literature (old, pre-this paper) were built by and for freeway (data)
	- urban arterials are more complex due to signalization (traffic signalization \[stop, go])
		- CIDM approaches account for this however, especially at areas where analytical approaches fail as demonstrated by Qiao et al 2001 using a neural network-based system identification approach, verified by data simulation and field testing
		- NN error range 22.39%
		- 24.74% error range for geometric and normal distribution model
	- road network level still difficult, in part due to covering enough part of the road network with sensors
		- 

### what problem does it solve

Long term traffic forecasting used for urban planning

# normalizing flow models


### what are alternatives

- what problem does short term traffic forecasting solve? what are the most used methodologies to solve this problem? what are the best performing models recently used to solve this problem?

### Types of short-term traffic forecasting
#### model-based
#### data driven
#### streaming data driven

## What are the models used in data driven short-term traffic forecasting
### Statistical
### AI-based
### Hybrid