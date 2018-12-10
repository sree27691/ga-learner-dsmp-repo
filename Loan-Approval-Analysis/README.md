### Project Overview

 Dream Housing Finance Inc. specializes in home loans across different market segments - rural, urban and semi-urban. Thier loan eligibility process is based on customer details provided while filling an online application form. To create a targeted marketing campaign for different segments, they have asked for a comprehensive analysis of the data collected so far.

The dataset has details of 614 customers with the following 13 features
Feature 	Description
Loan_ID 	Unique Loan ID
Gender 	Male/Female
Married 	Applicant Married (Y/N)
Dependents 	Number of dependents
Education 	Graduate/Under Graduate
Self_Employed 	Self employed (Y/N)
ApplicantIncome 	Income of the applicant
CoapplicantIncome 	Income of the co-applicant
LoanAmount 	Loan amount in thousands
LoanAmountTerm 	Term of loan in months
Credit_History 	credit history meets guidelines}
Property_Area 	Urban/Semi-Urban/Rural
Loan_Status 	Loan approved (Y/N)

Our major work for this project involves data analysis using Pandas.



### Learnings from the project

 - We can see that Loan_ID, Gender, Married, Dependents, Education, Self_Employed, Property_Area, Loan_Area these are categorical variables. ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History these are numerical variables. 

- The gender-based average loan amount of a person based on their employee status is as below                              
Gender       Married     Self_Employed  LoanAmount            
Female                     No           No             114.768116
                                    No          Yes            125.272727
                                    Yes         No             133.714286
                                    Yes         Yes            282.250000
Male                          No          No             129.508621
                                    No          Yes            180.588235
                                   Yes          No             152.608150
                                   Yes         Yes            167.420000

- The number of People who are self-employed and have a loan is 56
- The number of People who are not self-employed and have a loan is 366
- The percentage of loan approval for self employed people 9.12 %
- The percentage of loan approval for people who are not self-employed 59.61%
- The number of applicants based on loan term given  greater than or equal to 25 years is 554
- The Average income and credit score required to get a loan approval. 

Loan_Status        ApplicantIncome  Credit_History                         
N                                  5446.078125        0.572917
Y                                    5384.068720        0.983412



### Approach taken to solve the problem

 -  In this project major principles used are as below 
    Dataframe slicing
    Dataframe aggregation
    Pivot table operations
   




### Challenges faced

 NA


### Additional pointers

 NA


