# This is a sample Python script.
import glob
import sys
import pandas as pd
import matplotlib.pyplot as plt
import functions as local
from functions.functions import print_histogram, print_pie
from numpy import ma


if __name__ == '__main__':
    df1 = pd.read_csv(sys.argv[1])
    df1['InvoiceDate'] = pd.to_datetime(df1.InvoiceDate, yearfirst=True)
    df1['InvoiceDate'] = df1['InvoiceDate'].dt.date
    df1['InvoiceDate'] = pd.to_datetime(df1.InvoiceDate)
    # Canceled
    # df1 = df1[df1.Invoice.str.startswith('C') != True]
    # df1 = df1[df1.Price > 0]
    # print(df1.count())
    # print_pie([dfTmp, df1['Invoice'].count()], legend=['Canceled', 'All']) 1050797
    # Canceled and no price delete
    df1 = df1[df1.Invoice.str.startswith('C') != True]
    df1 = df1[df1.Price > 0]
    # Nan
    # values = df1.isna().sum()
    # print_histogram(values.index, values.values, legend=['Nan'])
    # print_pie([max(values.values), df1['Invoice'].count()], legend=['Nan', 'All'])
    df1['Customer ID'] = df1['Customer ID'].notna()
    # values = df1['Customer ID'].value_counts()
    # print_pie([values[0], values[1]], legend=values.index)
    # Max Min

    # Holidays data set init
    dfHolidays = pd.read_csv(sys.argv[2])
    dfHolidaysDay = pd.read_csv(sys.argv[3])
    dfHolidays['date'] = pd.to_datetime(dfHolidays.date, dayfirst=True)
    dfHolidaysDay['date'] = pd.to_datetime(dfHolidaysDay.date, dayfirst=True)
    df1['DateYear'] = df1.InvoiceDate.dt.year
    df1['DateMonth'] = df1.InvoiceDate.dt.month
    df1['DateDay'] = df1.InvoiceDate.dt.day
    # Merge with UK holidays
    dfTmp = df1.merge(dfHolidays, how='left', left_on='InvoiceDate', right_on='date')
    dfTmp.drop(['name'], axis=1, inplace=True)
    dfTmp['Day_of_holiday'] = dfTmp['date'].notna()
    dfTmp.drop(['date'], axis=1, inplace=True)
    # Merge with Uk pre Holidays days
    dfTmp = dfTmp.merge(dfHolidaysDay, how='left', left_on='InvoiceDate', right_on='date')
    dfTmp.drop(['name'], axis=1, inplace=True)
    dfTmp['Days_of_pre_holiday'] = dfTmp['date'].notna()
    dfTmp.drop(['date'], axis=1, inplace=True)
    # Deleting InvoiceDate
    dfTmp.drop(['InvoiceDate'], axis=1, inplace=True)
    # Saving to file
    dfTmp.to_csv('../data/new_data/retail.csv')


