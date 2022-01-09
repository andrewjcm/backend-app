# C964: Computer Science Capstone
### Backend: Django REST Framework
Frontend found here: <https://github.com/andrewjcm/frontend-app> <br/>
Deployed app: <https://covid-survival-guide.herokuapp.com>
***
####User Guide
1. Open your browser and navigate to <https://covid-survival-guide.herokuapp.com>
2. View three data descriptive visualizations on the home page
3. Click on “Dashboard”
4. Login with test user credentials: (username: test, password: test)
5. Fill out the form with a minimum of age and sex
6. Click submit
7. View prediction 
***

###Problem Statement 

COVID-19 pandemic has many people living in fear. From the beginning of the spread, many questioned whether contracting the virus could be fatal. Unfortunately, for many worldwide, the virus has proven to be fatal. As a result, there is a high demand for a product to clear up those questions.  

###Customer Summary 

The potential client base is virtually limitless: the individual, the doctor, the policymakers, and the employer. With the ability to address isolated cases and assess risk, all of these types of clients would benefit. The proposed application would allow various kinds of clients to address mortality concerns when confronted with a COVID case. 

###Existing System Analysis 

Currently, there are no applications that provide this type of solution. As a result, public health officials worldwide have lost the trust of their countrymen. With much uncertainty, sometimes ignorance, changes in policy and lack of transparency have caused the public to distrust those that were thought to have authority in the subject. A product with transparency solely focused on science would be welcomed by society. 

###Data  

The raw dataset was initially acquired from the Mexican government's public database. It was since published on the website Kaggle.com. The data used by the application was downloaded from Kaggle.com and stored as a CSV file. The data is then processed by converting the “yes” or “positive” to 1 and “no” or “negative” to a 0. Then multiple columns, which had "unknown" as most of their values, were dropped. The dropped columns were "pregnancy," "ventilator," "covid_contact," and "ICU." From there, any records that had null values within their columns were also dropped. Finally, the columns were dropped to remove any inconclusive data. After cleaning the data, there were still over two hundred thousand records to train the machine learning algorithm.

###Data Product Code 

The data were processed as stated in the prior section. Cleaning the data in this way assisted with the accuracy of the predictive method. From there, the data was described by using visual aids. Firstly, a basic bar chart presented the overall mortality rate of confirmed COVID cases. Second, the age distribution of all deaths was visualized in a line chart. Lastly, the distribution of all comorbidities was shown in the form of a pie chart. 

The predictive method was classified using logistic regression. First, the data was split between training data and test data. Then, features and outcome further broke it down. Finally, 70% of the total cleaned data was used to train the machine learning model. The features consisted of age, sex, and comorbidities and health risks. The outcome was whether the patient died or not. 
***
[Full write up](https://1drv.ms/b/s!Arf1cZfMTcHej_RpkqxzbOcFdtbfOQ "Link to writeup PDF in OneDrive")