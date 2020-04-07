# Prediction of COVID-19 Cases

# Team Members:
Aniruddha Sudhindra Shirahatti<br/>
Bharadwaj Aryasomayajula<br/>
Manoj Krishna Mohan<br/>
Sai Kumar Thallada<br/>
Ravi Teja Kolla

# Research question:  
With the upcoming rise in the global pandemic, we try to predict the upcoming number of cases which could be confirmed for a specific date. We also plan to predict the region across which the number of cases can increase. With our knowledge, we take on a challenging problem to solve a global case of emergency.

# Audience Definition:

The problem we are trying to solve is related to the global pandemic that the entire world is facing.

We have amassed a huge data spanning from January to the present day. This includes data from all the states, Counties with detailed information such as latitude and longitude.

By taking up this dataset, we aim mainly at forecasting the rise in the number of COVID-19 Cases across the United States being the main audience for the Problem statement. 

# Domain and Data: 
The domain of the data is Healthcare or more precisely diseases classification.
The dataset contains cumulative and non-cumulative count of confirmed, death and recovered global cases of COVID-19 (upto March 14, 2020), we expect the data to be populated again.
The dataset consists of 500,000 rows approximately and 11 columns **for each CSV**:
<br>
location      
county        
ship          
case_type   
cases         
country       
date          
difference    
latitude      
longitude     
state 

Since the dataset we have taken contains the global data of the pandemic COVID 19 affected, we have filtered the data based on the Country and have taken into account the cases only in the United States.

Link to dataset: https://www.tableau.com/covid-19-coronavirus-data-resources

## Preprocessing that may be necessary:
Preprocessing is included as a Jupyter Notebook which can be viewed in the GitHub site URL provided:
https://github.com/mkrish14/itcs6155_group14/blob/master/Deliverable_3/deliverable3.ipynb


- We dropped a few columns which are least corelated with the predicator variables and had only kept those columns which actually contribute in determining the target and help in the prediction analysis.
- The following is a list of all the columns that were dropped off
	* 'Admin2',
	* 'If Province Empty Country',
	* 'Select Metric',
	* 'Country Label',
	* 'LOG(SUM([Cases]))',
	* 'Select Metric Swapper',
	* 'Province_State Label (not US)',
	* 'Province_State Label (US)',
	* 'US Unassigned?',
	* 'US Out of Area?',
	* 'Metric Switcher',
	* 'Case Type 2',
	* 'Case Type Notes',
	* 'Combined_Key',
	* 'Province Label',
	* 'FIPS',
	* 'If Province Empty then ""',
	* 'LOG(Metric Switcher)',
	* 'Number of Records',
	* 'Prep Flow Runtime',
	* 'Select Metric Header Short',
	* 'Table_Names'

 - We have renamed a few columns for our convenience 
 - Since the column by name "County" had a preceding label "|County" we cleaned the data by removing the preceeding labels.
 - Since the date column was a string, we converted the entire column to a Pandas DateTime object.
 - We performed label encoding on the categorical data type objects to convert them into int data type.
 - As a last step of preprocessing we converted all the NaN values of the "difference" columns to zeroes.
  

The **EDA Dashboard** has been created using **Google Datastudio**. (https://github.com/mkrish14/itcs6155_group14/blob/master/Deliverable_3/ExploratoryDataAnalysis.pdf)

The data for plotting is stored in the *Google Cloud Storage Bucket*, which is later on imported to the DataStudio.

We have plotted three different plot to visualize the data:
- **Line plot** (along with a trendline which is exponential).
We ploted a line plot against the cases vs Data which depicts an exponential growth of the increase in number of COVID-19 cases. From the graph, it can be infered that there was a spike/increase in the number of positive cases in the 3rd week of March following an exponential trend line
- A **GeoPlot/GeoMap Plot** which indicates which regions of the United States are affected more.
We plotted a geo Map which shows the maximium afftected states in the United States. This is the contrast of the red color in the geo map.
From the graph, it is clearly evident that how the states of US are affected based on the color contrast. As wee can see states like North Carolina, Wisconsin, Arizona, Alabama to be in light contrast when compared to mid range affected states like California, Florida and Washington. New York is the most affected state with no other state matching the color contrast.
- A **Pie Chart** which shows how much percentage of People with Confirmed Active COVID-19 Cases are present and number of Deaths in the US.
From the chart, it can be inferred that 97.9% (https://www.worldometers.info/coronavirus/country/us/) are the confirmed cases and the rest 2.1 % are the total number of deaths occured across the nation.


<!-- ## size of data - data must be “big” data (millions of records) -->

## Tentative plan for analysis on GCP:

#### 1. GCP further processing - ML
We are going to implement various CART Algorithms(Classification and Regression Treees) to predict the accuracy and correctness of the machine learning model implemented.

#### 2. Evaluation of results
We are planning to use following evaluation metrics for evaluating the accuracy of ML model in our project:
1. R2 Score
2. Mean Squared Error (MSE)
3. Mean Absolute Error (MAE)
4. Confusion Matrix
5. Area Under Curve (AUC)
#### 3. Final Dashboard for User Group
We are planning to perform analysis on the data by creating easy to interpret dashboard on Google Data Studio for the User Group.

## Completed Set of Tasks

#### EDA
#### Pre-Processing

## Research Citations

[1] https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(20)30243-7/fulltext <br/>
[2] https://console.cloud.google.com/marketplace/details/johnshopkins/covid19_jhu_global_cases <br/>
[3] https://www.fredhutch.org/en/news/center-news/2020/03/coronavirus-latest-scientific-research.html <br/>
[4] https://www.accuweather.com/en/weather-blogs/weathermatrix/analysis-of-new-research-paper-tying-coronavirus-to-weather/703270 <br/>

