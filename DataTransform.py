import datetime as datetime
import pandas as pd
loans_df = pd.read_csv('loan_payments.csv')

# This class handles all the column conversions to the appropriate format
class DataTransform:
    
    def __init__(self, loans_df):
        self.loans_df = loans_df

        
        del loans_df['Unnamed: 0']

    def loans_df_transform(loans_df):
        loans_df = loans_df.astype({'issue_date':'datetime64[ns]','earliest_credit_line':'datetime64[ns]',
                          'last_payment_date':'datetime64[ns]', 'next_payment_date': 'datetime64[ns]', 
                          'last_credit_pull_date':'datetime64[ns]'})
    loans_df_transform(loans_df)