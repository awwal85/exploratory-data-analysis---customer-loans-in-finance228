import numpy as np
import pandas as pd
import seaborn as sns

loans_df = pd.read_csv('loan_payments.csv')

class DataFrameTransform:
    def __init__(self, loans_df):
        self.loans_df = loans_df
    
    def transformation(loans_df):
        null_values = round(100 * (loans_df.isna().mean()), 2)
        print(f"\n The null values with respective percentages in each column are shown below {null_values}")

        # Drop funded_amount and funded_amount_inv columns since they are duplicates of the loan_amount column. 
        # Drop columns with more than 50% of missing data and columns that are irrelevant to our to analysis 
        # yet with some missing values
        loans_df = loans_df.drop(['id', 'member_id', 'funded_amount', 'funded_amount_inv', 'mths_since_last_record', 
                                'mths_since_last_major_derog','mths_since_last_delinq', 'last_payment_date',
                                'collections_12_mths_ex_med', 'sub_grade','out_prncp_inv', 'total_payment_inv', 
                                'policy_code', 'next_payment_date', 'total_rec_late_fee', 
                                'recoveries', 'collection_recovery_fee'], axis = 1)

    def impute_columns(loans_df):
        loans_df['term'] = loans_df['term'].fillna(loans_df['term'].mode())
        loans_df['int_rate'] = loans_df['int_rate'].fillna(loans_df['int_rate'].mean())
        loans_df['employment_length'] = loans_df['employment_length'].fillna(loans_df['employment_length'].mode())

        #Remove the missing rows by using the not null records functions
        loans_df = loans_df[loans_df['last_credit_pull_date'].notnull()]
        
    # Transformation on skewed columns. I used the log transform because they are right skewed, and is a strong transformation
    # with major effect on distribution shape.
    def transform_skewed_columns(loans_df):
        loans_df['total_payment'] = loans_df['total_payment'].map(lambda i: np.log(i) if i > 0 else 0)
        loans_df['total_rec_prncp'] = loans_df['total_rec_prncp'].map(lambda i: np.log(i) if i > 0 else 0)
        loans_df['total_rec_int'] = loans_df['total_rec_int'].map(lambda i: np.log(i) if i > 0 else 0)
    
    #Remove outliers
    def remove_outliers(loans_df):
        numeric_variables = ['loan_amount', 'int_rate', 'instalment', 'annual_inc',
                             'dti', 'inq_last_6mths', 'open_accounts', 'total_accounts', 'out_prncp',  
                             'total_payment', 'total_rec_prncp', 'total_rec_int', 'last_payment_amount']
        Q1 = loans_df[numeric_variables].quantile(0.25)
        Q3 = loans_df[numeric_variables].quantile(0.75)
        IQR = Q3 - Q1

        loans_df = loans_df[~((loans_df[numeric_variables] < (Q1 - 1.5 * IQR)) |
                              (loans_df[numeric_variables] > (Q3 + 1.5 * IQR))).any(axis=1)]

    def target_variables(loans_df):
        # Extract quantitative variables from the loans_df
        quant_df = loans_df.select_dtypes(include = ['float64', 'int64'])
        loans = quant_df.copy()
        # Extract qualitative variables from the loans_df
        qual_df = loans_df.select_dtypes(include = ['O'])
        # Add target variables to the quantitative variables
        cols = ['loan_status', 'home_ownership', 'purpose', 'grade']
        loans[cols ] = qual_df[cols ]
        print(f'\n The target variables are {loans.columns}')

DataFrameTransform(loans_df)