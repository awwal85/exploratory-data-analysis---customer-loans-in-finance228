class DataFrameInfo:
    import pandas as pd

    loans_df = pd.read_csv('loan_payments.csv')
    loans_df.dtypes
    loans_df.describe()
    loans_df.select_dtypes(exclude=["number","bool_", "datetime64[ns]"])
    loans_df.shape
    counts = loans_df.isna().sum()
    percentages = round(loans_df.isna().mean() * 100, 2)
    null_values = pd.concat([counts, percentages], axis = 1, keys = ["count", "%"])
    print(null_values)
