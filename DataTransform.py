import datetime as datetime
import pandas as pd
# This class handles all the column conversions to the appropriate format
class DataTransform:
    loans_df = pd.read_csv('loan_payments.csv')
    del loans_df['Unnamed: 0']
    df = loans_df.astype({'issue_date':'datetime64','earliest_credit_line':'datetime64',
                          'last_payment_date':'datetime64', 'next_payment_date': 'datetime64', 
                          'last_credit_pull_date':'datetime64'})