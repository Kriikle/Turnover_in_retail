import sys

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

if __name__ == '__main__':

    df2 = pd.read_csv('../data/new_data/time_sires.csv', index_col=0)
    df2.index = pd.to_datetime(df2.index)

    t = sys.argv[1]
    df2 = df2.resample(t).sum()
    if len(sys.argv) > 2:
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

