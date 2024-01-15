import DataFrameTransform
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Analysis:
    def __init__(self, loans):
        self.loans = loans

    def analysis_and_visual(loans):
        DataFrameTransform.target_variables
        loans_fully_paid = loans.query("loan_status == 'Fully Paid'")['loan_amount'].sum()
        loans_charged_off = loans.query("loan_status == 'Charged Off'")['loan_amount'].sum()
        total_loans = loans['loan_amount'].sum()
        total_loans_count = loans['loan_amount'].count()
        fully_paid_per = round(loans_fully_paid/total_loans*100, 2)
        charged_off_per = round(loans_charged_off/total_loans*100, 2)

        # percentage of loans that are currently behind
        loans_currently_behind = loans.query("loan_status != 'Fully Paid' and loan_status != 'Charged Off' ")['loan_amount'].sum()
        loans_currently_behind_per = round(loans_currently_behind/total_loans*100, 2)

        # Percentage of loans that are late and charged off
        loans_currently_behind_count = loans.query("loan_status == 'Late' or loan_status == 'Charged Off' ")['loan_amount'].count()
        loans_currently_behind_total = loans.query("loan_status == 'Late' or loan_status == 'Charged Off' ")['loan_amount'].sum()
        users_currently_behind_per = round(loans_currently_behind_count/total_loans_count, 2)
        print(f" \n {fully_paid_per}% of loans are fully paid")
        print(f"\n {charged_off_per}% of loans are charged off")
        print(f"\n The percentage of loans that are currently behind is {loans_currently_behind_per}")
        print(f"\n {loans_currently_behind_count} users are currently behind in servicing their loans")
        print(f"\n The percentage of users that are either late or charged off is {users_currently_behind_per}% and would amount to £{loans_currently_behind_total} of loss if the late users default in paying.")
    
        # Checking how the grade could affect loan servicing 
        plt.figure(figsize=(12,5))
        grade_order = sorted(loans['grade'].unique())
        sns.countplot(x = 'grade', data= loans, hue = 'loan_status', order = grade_order)
        plt.show()
        print(f"\n Clearly, the grade has no effect on users inability of payoff loans")

        # Checking how the purpose could affect loan servicing
        plt.figure(figsize=(12,5))
        grade_order = sorted(loans['purpose'].unique())
        sns.countplot(x = 'purpose', data= loans, hue = 'loan_status', order = grade_order)
        plt.show()
        print(f"\n The purpose of loan has no effect on loans that are charged off")

        # Checking how the home_ownershp could affect loan servicing
        plt.figure(figsize=(12,5))
        grade_order = sorted(loans['home_ownership'].unique())
        sns.countplot(x = 'home_ownership', data= loans, hue = 'loan_status', order = grade_order)
        plt.show()
        print(f"\n The home ownership has effect on loans that are charged off, particularly for mortgage, own and rent cateories")   
        Analysis(loans)