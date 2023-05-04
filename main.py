# This is a sample Python script.
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from sklearn.metrics import r2_score
import functions as local
import statsmodels.api as sm
from scipy import stats
import seaborn as sns
from functions.functions import print_histogram, print_pie
from numpy import ma


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df1 = pd.read_csv('data/new_data/retail.csv', index_col=0, dtype={'Invoice': str, 'Quantity': float})
    df2 = pd.read_csv('data/new_data/time_sires.csv', index_col=0)
    df2.index = pd.to_datetime(df2.index)

    # sns.lineplot(x=df2.index, y=df2['Trade_over'])
    # # plt.xlim(0, 1000)
    # plt.show()

    value1 = df1['Day_of_holiday'].value_counts()
    value2 = df1['Days_of_pre_holiday'].value_counts()

    # Nan
    values = df1.isna().sum()
    # print_histogram(values.index, values.values, legend=['Пустые'])
    # print_pie([max(values.values), df1['Invoice'].count()], legend=['Пустые', 'Всего'])
    # values = df1['Customer ID'].value_counts()

    # print_pie([values[0], values[1]], legend=values.index)
    # dfMax = pd.DataFrame(df1.values.max(0)[None, :], columns=df1.columns).T
    # dfMin = pd.DataFrame(df1.values.min(0)[None, :], columns=df1.columns).T
    # dfMean = pd.DataFrame(df1.values.mean(0)[None, :],
    #                       columns=['Quantity', 'DateYear', 'DateMonth', 'DateDay', ]
    #                     )
    # print(dfMax)
    # print(df1['Country'].value_counts())
    # values = df1['Country'].value_counts()
    # plt.pie(values.values, labels=values.index)
    # plt.show()

    df2 = df2.resample('W').sum()
    print(df2)
    arma_ = sm.tsa.ARIMA(df2, order=(5, 0, 0)).fit()
    resid = arma_.resid
    predict = arma_.predict("2009-12-06", "2011-12-11")
    print(arma_.summary())
    r2 = r2_score(df2.values, predict.values)
    print('R^2: %1.2f' % r2)
    plt.plot(predict.index, predict.values)
    plt.plot(df2.index, df2.values)
    plt.legend(['Прогноз', 'Изначальный ряд'])
    plt.show()

    # # predict = arma_.simulate(200)
    # plt.plot(predict.index, predict.values)
    # plt.plot(df2.index, df2.values)
    # plt.legend(['Прогноз'])
    # plt.show()
    # print(arma_.params)



    # stats.normaltest(resid)
    # fig = plt.figure(figsize=(12, 8))
    # ax = fig.add_subplot(111)
    # fig = qqplot(resid, line="q", ax=ax, fit=True)
    # plt.show()


    # print(df1['StockCode'].value_counts())
    # df1 = df1[df1.StockCode == '85123A']
    # print(df1['Description'].())
    # print(df1['Price'].value_counts())
    # print(dfMin)
    # df1 = df1[df1.Price < 100]
    # df1 = df1[df1.Quantity < 100]
    # print(df1.count())
    # sns.boxplot(df1, x='DateMonth', y='Quantity', hue='DateYear')
    # sns.boxplot(df1, x='DateMonth', y='Price', hue='DateYear')
    # plt.ylim(0, 1000)
    # # df1[['Quantity', 'Price', 'Customer ID', 'DateYear', 'DateMonth', 'DateDay', 'Day_of_holiday', 'Days_of_pre_holiday']]
    # # print()
    # # sns.heatmap(df1.corr(), annot=True)
    # plt.show()

    # print_pie([value1[0], value1[1]], legend=['Совпали с праздником', 'Остальные'])
    # print_pie([value2[0], value2[1]], legend=['Препразднечные', 'Остальные'])

    # value_of_column_1 = df1[df1.DateYear == 2009].DateMonth.value_counts()
    # value_of_column_2 = df1[df1.DateYear == 2010].DateMonth.value_counts()
    # value_of_column_3 = df1[df1.DateYear == 2011].DateMonth.value_counts()
    # print_histogram(
    #     value_of_column_1.index,
    #     value_of_column_1.values,
    #     value_of_column_2.index,
    #     value_of_column_2.values,
    #     value_of_column_3.index,
    #     value_of_column_3.values,
    #     legend=['2009', '2010', '2011'],
    # )
