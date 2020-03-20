# Prediction of Rate of Cases due to Novel CoronaVirus(COVID-19)


# Team Members:
Aniruddha Shirahatti.<br/>
Bharadwaj Aryasomayajula. <br/>
Manoj Krishna Mohan. <br/>
Sai Kumar Thallada. <br/>
Ravi Teja Kolla. 

# Research question:  
With the upcoming rise in the global pandemic, we try to predict the upcoming number of cases which could be confirmed for a specific date. We also plan to predict the region across which the number of cases can increase. With our knowledge, we take on a challenging problem to solve a global case of emergency.
# Domain and Data: 
The domain of the data is Healthcare or more precisely diseases classification.
The dataset contains cumulative and non-cumulative count of confirmed, death and recovered global cases of COVID-19 (upto March 14, 2020), we expect the data to be populated again.
The dataset consists of 70K rows approximately and 8 columns **for each CSV**:
Country/RegionCountry/Region<br/>
Province/StateProvince/State<br/>
LatLatitude<br/>
LongLongitude<br/>
DateDate<br/>
StatusConfirmed, Deaths or Recovered<br/>
CumulitiveCasesCumulative number of cases<br/>
CasesNon-cumulative number of cases (Daily cases)<br/>

Link to dataset: https://www.kaggle.com/devready/2019-novel-coronavirus-2019ncov/version/6#2019-nCoV%20(14-Mar-2020).csv

## Preprocessing that may be necessary:
- Since we have 4 CSV files, we need to concatenate them, in order to predict the next occurence of confirmed cases or deaths.
- We also plan to perform binning dataset, where we categorize the data by changing the Province column to another column called as Region as in, *ASIA, EUROPE, MIDDLE-EAST, NORTH AMERICA, SOUTH AMERICA, AUSTRALIA*

Thus by carrying out the above PreProcessing steps, our data will be ready for the next task of Training the Machine Learning Model.

<!-- ## size of data - data must be “big” data (millions of records) -->

## Tentative plan for analysis on GCP

#### 1. EDA and Preprocessing

#### 2. GCP further processing - ML

#### 3. Evaluation of results

#### 4. Final Dashboard for User Group
