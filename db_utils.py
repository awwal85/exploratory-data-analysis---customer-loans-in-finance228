import datetime as datetime
import pandas as pd
import sqlalchemy as db
from sqlalchemy import create_engine
import yaml

class RDSDatabaseConnector:
    with open('credentials.yaml') as f:
        credentials_file = yaml.safe_load(f)
        
    def __init__(self,credentials_file):
        self.credentials.yaml = credentials_file
    
        # Extracting data from the RDS database as a Pandas DataFrame
        engine = create_engine('postgresql://loansanalyst:EDAloananalyst@eda-projects.cq2e8zno855e.eu-west-1.rds.amazonaws.com:5432/payments')
        conn = engine.connect()
        table_df = pd.read_sql_table("loan_payments", con = engine) 
        print(table_df)

        # Saves the data as a csv file in my local machine
        table_df.to_csv(r'C:\Users\Cex- pc\oneDrive\Desktop\Data Analysis\loan_payments.csv')

        #  Loading the data from my local machine into a Pandas DataFrame.
        loans_df = pd.read_csv('loan_payments.csv')
        del loans_df['Unnamed: 0']
        loans_df.head()