import matplotlib.pyplot as plt
import pandas as pd

def check_missing_values(df):
    return df.isnull().sum()[df.isnull().sum() > 0]

def plot_histograms(df, columns):
    plt.figure(figsize=(15, 10))
    for i, col in enumerate(columns, 1):
        plt.subplot(2, 3, i)
        if df[col].dtype == 'object' or df[col].dtype.name == 'category':
            df[col].value_counts().plot(kind='bar')
            plt.title(f'Distribution of {col}')
        else:
            df[col].hist(bins=30)
            plt.title(f'Distribution of {col}')
        plt.xlabel(col)
    plt.tight_layout()
    plt.show()

def date_validation(date_column):
    valid_dates = 0
    invalid_dates = 0
    for date_str in date_column:
        try:
            pd.to_datetime(date_str, format="%Y-%m-%d")
            valid_dates += 1
        except ValueError:
            invalid_dates += 1
    return valid_dates, invalid_dates

