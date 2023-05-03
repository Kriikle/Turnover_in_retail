# This is a sample Python script.
import sys

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

if __name__ == '__main__':
    df1 = pd.read_csv('../data/new_data/retail.csv', index_col=0, dtype={
        'Invoice': str,
        'Quantity': float,
        'name': str,
        'Country': str
    })
    df_dates = pd.read_csv('../data/dates.csv')
    df_dates['date'] = pd.to_datetime(df_dates.date, dayfirst=True)
    df1['InvoiceDate'] = pd.to_datetime(df1.InvoiceDate, yearfirst=True)

    df1['Trade_over'] = df1['Price'] * df1['Quantity']
    # df1 = df_dates.merge(df1, how='left', left_on='date', right_on='InvoiceDate')
    df1[['InvoiceDate', 'Trade_over']].groupby(['InvoiceDate']).sum().to_csv('../data/new_data/time_sires.csv')


