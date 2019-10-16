# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)

categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)

# code ends here


# --------------
# code starts here
banks = bank.drop('Loan_ID', axis=1)

print(banks.ApplicantIncome.isnull().sum())
print(banks.CoapplicantIncome.isnull().sum())
print(banks.LoanAmount.isnull().sum())
print(banks.Loan_Amount_Term.isnull().sum())

bank_mode = banks.mode

banks = banks.fillna(bank_mode)

print(banks.ApplicantIncome.isnull().sum())
print(banks.CoapplicantIncome.isnull().sum())
print(banks.LoanAmount.isnull().sum())
print(banks.Loan_Amount_Term.isnull().sum())


#code ends here


# --------------
# Code starts here

avg_loan_amount = banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'], values='LoanAmount', aggfunc=({'LoanAmount': 'mean'}))

# code ends here



# --------------
# code starts here
loan_approved_se = banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')]

loan_approved_nse = banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')]

loan_status_cnt = 614

percentage_se = (loan_approved_se.shape[0] / loan_status_cnt) * 100

percentage_nse = (loan_approved_nse.shape[0] / loan_status_cnt) * 100

# code ends here


# --------------
# code starts here

loan_term = banks.apply(lambda x: x.Loan_Amount_Term/12, axis=1)

big_loan_term = loan_term[loan_term >= 25].shape[0]

# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')

loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']

mean_values = loan_groupby.agg('mean')

# code ends here


