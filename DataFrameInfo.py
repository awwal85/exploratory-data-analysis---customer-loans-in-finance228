import pandas as pd
loans_df = pd.read_csv('loan_payments.csv')

class DataFrameInfo:
    
    def __init__(self, loans_df):
        self.loans_df = loans_df
        
    def get_loans_df_info(loans_df):
        counts = loans_df.isna().sum()
        percentages = round(loans_df.isna().mean() * 100, 2)
        distinct_count = loans_df.select_dtypes(exclude=["number","bool_", "datetime64[ns]"])
        null_values = pd.concat([counts, percentages], axis = 1, keys = ["count", "%"])
        print(f"\nThe statistics of the loans data are {loans_df.describe()}")
        print(f"\n The shape of the data is {loans_df.shape} {loans_df.dtypes}")
        print(f"\n The data has the following data types{loans_df.dtypes}")
        print(f"\n The null values with respective percentages in each column are shown below {null_values}")
        print(f"\n The count of distinct values in categorical columns {distinct_count}")
    get_loans_df_info(loans_df)
