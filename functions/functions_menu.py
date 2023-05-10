import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from sklearn.metrics import r2_score
import statsmodels.api as sm


def create_time_sires():
    df1 = pd.read_csv('data/new_data/retail.csv', index_col=0, dtype={
        'Invoice': str,
        'Quantity': float,
        'name': str,
        'Country': str
    })
    df1['InvoiceDate'] = pd.to_datetime(df1.InvoiceDate, yearfirst=True)
    df1['Trade_over'] = df1['Price'] * df1['Quantity']
    df1[['InvoiceDate', 'Trade_over']].groupby(['InvoiceDate']).sum().to_csv('data/new_data/time_sires.csv')


def anilisis_time_siris(t='D', flg_print=None):
    df2 = pd.read_csv('data/new_data/time_sires.csv', index_col=0)
    df2.index = pd.to_datetime(df2.index)

    df2 = df2.resample(t).sum()
    if flg_print is not None:
        mean_window = int(df2.count() / 20)
        plt.plot(df2.index, df2.values)
        plt.plot(df2.index, df2.Trade_over.rolling(window=mean_window).mean())
        plt.legend(['Time series', 'Moving average for (' + str(mean_window) + ')t'])

        plot_acf(df2.values)
        plot_pacf(df2.values, method='ywm')
        decompose = seasonal_decompose(df2)
        decompose.plot()
        plt.show()

    adf_result = adfuller(df2.values, regression='c')
    print('adf: ', adf_result[0])
    print('p-value: ', adf_result[1])
    print('Critical values: ', adf_result[4])
    if adf_result[0] > adf_result[4]['5%']:
        print('There are unit roots, the series is not stationary')
    else:
        print('There are no unit roots, the series is stationary')


def pre_process_data(
        path_to_main_ds='data/online_retail_II(2).csv',
        path_to_holiday_ds='data/holidays.csv',
        path_to_holiday_pre_ds='data/holidays_pre.csv'
):
    df1 = pd.read_csv(path_to_main_ds)
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
    dfHolidays = pd.read_csv(path_to_holiday_ds)
    dfHolidaysDay = pd.read_csv(path_to_holiday_pre_ds)
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
    # dfTmp.drop(['name'], axis=1, inplace=True)
    dfTmp['Days_of_pre_holiday'] = dfTmp['date'].notna()
    dfTmp.drop(['date'], axis=1, inplace=True)
    # Deleting InvoiceDate
    # dfTmp.drop(['InvoiceDate'], axis=1, inplace=True)
    # Saving to file
    dfTmp.to_csv('data/new_data/retail.csv')


def forecasting(t='D', q=5, d=0, p=0):
    time_sires = pd.read_csv('data/new_data/time_sires.csv', index_col=0)
    time_sires.index = pd.to_datetime(time_sires.index)
    time_sires = time_sires.resample(t).sum()
    print(time_sires)
    arma_ = sm.tsa.ARIMA(time_sires, order=(q, d, p)).fit()
    resid = arma_.resid
    predict = arma_.predict(time_sires.index.min(), time_sires.index.max())
    print(arma_.summary())
    r2 = r2_score(time_sires.values, predict.values)
    print('R^2: %1.2f' % r2)
    plt.plot(predict.index, predict.values)
    # plt.plot(df2.index, df2.values)
    plt.legend(['Forecast', 'Time sires'])
    plt.show()
