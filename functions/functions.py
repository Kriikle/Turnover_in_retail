import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller


def print_histogram(x1, height1, x2=None, height2=None, x3=None, height3=None, legend=None, x_name='x', y_name='y'):
    if legend is None:
        legend = ['First', 'Second', 'Third']
    width = 1
    if height2 is not None and x2 is not None and height3 is not None and x3 is not None:
        x1 = x1 - 0.3
        x3 = x3 + 0.3
        width = 0.3
    if (height2 is not None and x2 is not None) and (height3 is None and x3 is None):
        x1 = x1 - 0.2
        x2 = x2 + 0.2
        width = 0.6
    plt.bar(x1, height1, width=width, color='#00539CFF', alpha=0.5, label=legend[0])
    if height2 is not None and x2 is not None:
        plt.bar(x2, height2, width=width, color='#EEA47FFF', alpha=0.5, label=legend[1])
    if height3 is not None and x3 is not None:
        plt.bar(x3, height3, width=width, color='#F96167', alpha=0.5, label=legend[2])
    plt.legend()
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.show()


def print_pie(values, legend=None):
    values_sum = sum(values)
    present = ['%.2f' % (value / values_sum) for value in values]
    plt.pie(values, labels=present, colors=['#FFC154', '#47B39C'])
    if legend is not None:
        plt.legend(legend, loc='upper right')
    plt.show()


def adf_test(df2, regression='c'):
    adf_result = adfuller(df2.values, regression=regression)
    if adf_result[0] > adf_result[4]['5%']:
        return False
    else:
        return True
