# --------------
# Code starts here

avg_loan_amount=banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'],values=['LoanAmount'],aggfunc='mean')


# code ends here



# --------------
# code ends here
loan_groupby= banks.groupby(['Loan_Status'])['ApplicantIncome', 'Credit_History']

# for printing groupby object
for key, item in loan_groupby:
    print(loan_groupby.get_group(key), "\n\n")

# finding the mean of loan groupby
type(loan_groupby)
mean_values=loan_groupby.mean()
# code ends here


# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank=pd.read_csv(path)
bank.head()
print(type(bank))
df=bank.columns
categorical_var=bank.select_dtypes(include=['object'])
print(categorical_var)
numerical_var=bank.select_dtypes(include=['number'])
print(numerical_var)





# code ends here


# --------------
# code starts here

loan_term=banks['Loan_Amount_Term'].apply(lambda x: x/12)

big_loan_term=loan_term[loan_term >= 25].value_counts().sum()
big_loan_term


# code ends here


# --------------
# code starts here
#loan_approved_se =banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')].count()
#print(loan_approved_se)

#df1=banks[banks['Self_Employed'] == Yes and banks['Loan_Status'] == Y]
#loan_approved_nse =banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')].count()
#print(loan_approved_nse)

#Loan_Status=614

#percentage_se=(loan_approved_se/Loan_Status)*100

#percentage_nse=(loan_approved_nse/Loan_Status)*100

#print(percentage_se)
#print(percentage_nse)

df1=banks['Self_Employed'] == 'Yes'
df2=banks['Loan_Status'] == 'Y'
df3=banks['Self_Employed'] == 'No'

loan_approved_se=len(banks[df1 & df2])
loan_approved_nse=len(banks[df2 & df3])



percentage_se=loan_approved_se/614*100

percentage_nse=loan_approved_nse/614*100
#print(loan_approved_se)
#print(loan_approved_nse)
#print(percentage_se)
#print(percentage_nse)


# code ends here


# --------------
# code starts here
banks=bank.drop('Loan_ID',axis=1)
print(banks.columns)
df=banks.isnull().sum()
print(df)
bank_mode=banks.mode()
print(bank_mode)
banks=banks.fillna(bank_mode.ix[0])
print(banks.isnull().sum())

#code ends here


