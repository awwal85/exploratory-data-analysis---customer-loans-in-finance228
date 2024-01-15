import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import DataFrameTransform
loans_df = pd.read_csv('loan_payments.csv')

class Plotter:
    def __init__(self, xvals = None, yvals = None):
        self.xvals = xvals
        self.yvals = yvals

    def plotthing(self):
        # Extract quantitative variables from the loans_df
        quant_df = loans_df.select_dtypes(include = ['float64', 'int64'])
        # Extract qualitative variables from the loans_df
        qual_df = [col for col in loans_df.columns if col not in quant_df ]
        sns.set(font_scale=0.7)
        f = pd.melt(loans_df, value_vars = quant_df )
        g = sns.FacetGrid(f, col="variable",  col_wrap=3, sharex=False, sharey=False)
        g = g.map(sns.histplot, "value", kde=True)
    
        print(qual_df)
    
    def corr_matrix(loans):
        DataFrameTransform.target_variables
        #factorize the category columns to find correlation
        labels, levels = pd.factorize(loans.loan_status)
        loans.loan_status = labels

        labels, levels = pd.factorize(loans.home_ownership)
        loans.home_ownership = labels

        labels, levels = pd.factorize(loans.purpose)
        loans.purpose = labels

        labels, levels = pd.factorize(loans.grade)
        loans.grade = labels

        #Plot the heatmap
        fig, ax = plt.subplots()
        fig.set_size_inches(24,8)
        sns.heatmap(loans.corr(), annot=True, fmt=".2f")
Plotter(loans_df)