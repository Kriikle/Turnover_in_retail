# This is a sample Python script.
import pandas as pd
import matplotlib.pyplot as plt
import functions as local
import seaborn as sns
from functions.functions import print_histogram, print_pie
from numpy import ma

if __name__ == '__main__':
    df1 = pd.read_csv('../data/new_data/retail.csv', index_col=0, dtype={
        'Invoice': str,
        'Quantity': float,
        'name': str
    })

    df1['Sum'] = df1['Price'] * df1['Quantity']
    df1[['InvoiceDate', 'Sum']].groupby(['InvoiceDate']).sum().to_csv('../data/new_data/time_sires.csv')



