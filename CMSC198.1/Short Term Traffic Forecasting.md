[[cmsc198.1root]]
[Excel File](https://docs.google.com/spreadsheets/d/1gOwl2GqrJP4o7FzvRvj-edDh6dKN5qYXAujqe5B9JpA/edit#gid=0)

```toc
```

## Short-term traffic forecasting: Where we are and where we’re going (2014) Vlahogianni et al

### Abstract 
Since the early 1980s, short-term traffic forecasting has been an integral part of most [Intelligent Transportation Systems](https://www.sciencedirect.com/topics/computer-science/intelligent-transportation-system "Learn more about Intelligent Transportation Systems from ScienceDirect's AI-generated Topic Pages") (ITS) research and applications; most effort has gone into developing methodologies that can be used to model traffic characteristics and produce anticipated traffic conditions. Existing literature is voluminous, and has largely used single point data from motorways and has employed univariate mathematical models to predict traffic volumes or travel times. Recent developments in technology and the widespread use of powerful computers and mathematical models allow researchers an unprecedented opportunity to expand horizons and direct work in 10 challenging, yet relatively under researched, directions. It is these existing challenges that we review in this paper and offer suggestions for future work.

### Intro
- STTF has been significant in transpo research for more than 3 decades
	- increasing need for developing user friendly applications which can provide both accurate info for drivers an d for signal optimization
		- ability to provide this is result of tech advancement
	- my guy proceeds to dozens of articles to drive this point home
- STTF based on data driven methods is one of the most dynamic and developing research arenas with enormous published literature
	- most of research concentrated on *testing* (in the paper’s exact words) alternative modeling approaches on STT data
		- possibly because data is readily available
		- relatively easy to apply many fo available analytical approaches
		- leaves a number of important questions unaddressed
		- paper discsusses 10 areas where technoloigcal and analytical challenges lie for the next generation fo STF research

### STTF: A brief overview
- integral part otf most intelligent transportation systems (IST) research
	- concerns predictions made from a few seconds to possibly few hours into the future 
		- based on developing methods that can be used to model traffic characteristics sucha as volume, density, and speed, or travel times, and produce traffic condition predictions 
	- has a life of 35 years since the first paper **Analysis of freeway traffic time-series data by using Box Jenkins techniques**  by Ahmed and Cook 1979
		- most employed classical statistical approaches
		- considered weak under:
			- unstable traffic conditions
			- complex road settings
			- extensive datasets of structured and unstructured 
	- Older studies relied on detectors for data collection
		- more recent studies come from GPS detectors, simulation, etc
		- traffic volume, travel time, and speed is studied
	- most effort has gone to **using data from motorways and freeways**
		- employing univariate statistical models
		- predicting traffic volume or travel time
		- using data collected from single ppint sources
	- recent development in tech allow researchers to expand to working on 10 challenges:
		- responsiveness and location of interest
		- forecasting traffic and variable choice
		- method and modeling issues involved with developing novel prediction algorithms
		- role of AI models

## An object-oriented neural network approach to short-term traffic forecasting - 2001 (Dia)
[https://www.sciencedirect.com/science/article/pii/S0377221700001259]
[https://doi.org/10.1016/S0377-2217(00)00125-9]

### Abstract
This paper discusses an object-oriented neural network model that was developed for predicting short-term traffic conditions on a section of the Pacific Highway between Brisbane and the Gold Coast in Queensland, Australia. The feasibility of this approach is demonstrated through a time-lag recurrent network (TLRN) which was developed for predicting speed data up to 15 minutes into the future. The results obtained indicate that the TLRN is capable of predicting speed up to 5 minutes into the future with a high degree of accuracy (90–94%). Similar models, which were developed for predicting freeway travel times on the same facility, were successful in predicting travel times up to 15 minutes into the future with a similar degree of accuracy (93–95%). These results represent substantial improvements on conventional model performance and clearly demonstrate the feasibility of using the object-oriented approach for short-term traffic prediction.

- study uses:
	- multilayer perceptrons
	- recurrent networks
	- TLRNs
	- Hybrid net

## Improving short-term traffic forecasts: to combine models or not to combine? (2015) Tselentis

### Abstract 
- This study compares the performance of statistical and Bayesian combination models with classical single time series models for short-term traffic forecasting.
- Combinations are based on fractionally integrated autoregressive time series models of travel speed with exogenous variables that consider speed's spatio-temporal evolution, and volume and weather conditions. 
- Several statistical hypotheses on the effectiveness of combinations compared to the single models are also tested. 
- Results show that, in the specific application, linear regression combination techniques may provide more accurate forecasts than Bayesian combination models. 
	- combining models with different degrees of spatio-temporal complexity and exogeneities is most likely to be the best choice in terms of accuracy. 
	- the risk of combining forecasts is lower than the risk of choosing a single model with increased spatio-temporal complexity.

### Notes

- trying to answer two specific questions:
	- What is the performance of the best possible combination of models compared to the performance of the best possible single model?
	- When the best single model is not known, what is riskier? To select a single model or combinations of forecasts?
- applied multiple models
	- ARIMA, ARIMAX, ARFIMA and ARFIMAX

## # Hybrid short-term traffic forecasting architecture and mechanisms for reservation-based Cooperative ITS (2021) - Zhang et al

### abstract
- Traffic forecasting is a critical challenge for [Intelligent Transportation Systems](https://www.sciencedirect.com/topics/engineering/intelligent-transportation-system "Learn more about Intelligent Transportation Systems from ScienceDirect's AI-generated Topic Pages") (ITS), increasingly enabled by the deepening interconnectedness of [intelligent vehicles](https://www.sciencedirect.com/topics/engineering/intelligent-vehicle-highway-systems "Learn more about intelligent vehicles from ScienceDirect's AI-generated Topic Pages") and traffic infrastructures.
- In this study, we propose a hybrid short-term forecasting architecture based on the careful consideration and analysis of reservation-based behavior cooperation and the characteristics of Cooperative ITS (C-ITS), especially its future application mode of Service-oriented C-ITS (SoC-ITS). 
- We design several novel models and mechanisms to forecast the behavioral parameters of road vehicles in this architecture, combining a developed [artificial neural network](https://www.sciencedirect.com/topics/engineering/artificial-neural-network "Learn more about artificial neural network from ScienceDirect's AI-generated Topic Pages") method and a statistical technique. 
- Considering the lack of large-scale deployment of C-ITS at present, a new simulator (SoC-ITSS v2.1) is independently designed with two main aims. The first is to establish a [massive dataset](https://www.sciencedirect.com/topics/computer-science/massive-datasets "Learn more about massive dataset from ScienceDirect's AI-generated Topic Pages") that is unavailable for current transportation systems, but necessary for [back propagation](https://www.sciencedirect.com/topics/engineering/backpropagation "Learn more about back propagation from ScienceDirect's AI-generated Topic Pages") neural network-based forecasting and statistics models.
- Our second aim is to provide an effective visual [verification environment](https://www.sciencedirect.com/topics/computer-science/verification-environment "Learn more about verification environment from ScienceDirect's AI-generated Topic Pages") for this proposed mechanism. 
- Using our newly developed simulator, these proposed models and methods are verified under two typical [authorization policies](https://www.sciencedirect.com/topics/computer-science/authorization-policy "Learn more about authorization policies from ScienceDirect's AI-generated Topic Pages") (First-Arrival-First-Pass-Multi-Queue for ordinary C-ITS and Highest-Weight-First-Pass-Multi-Queue for SoC-ITS). 
- The experimental results show that this forecasting mechanism can adaptively model traffic situations of both ordinary C-ITS and SoC-ITS, and provide good performance.


- **GOOGLE MAPS API google CLOUD**
- neural ordinary differential equations


- what is short term traffic forecasting
	- types of traffic forecasting
	- how does it differ
- what are models used in STTF
	- statistical models
	- deep learning
	- AI-based
	- hybrid
![[Pasted image 20230915133428.png|284]]