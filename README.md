# This program is designed to process a set of [data](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci?datasetId=430934) from kagle.
### Ds data:
![For years](https://github.com/Kriikle/Turnover_in_retail/blob/master/images/Histogram_years.png "Years and data")
Added data of holidays in UK from 2009 to 2011.[holidays.csv](https://github.com/Kriikle/Turnover_in_retail/blob/master/data/holidays.csv)
### The possibility of linear forecasting of trade turnover is being tested. (data has no correlate attributes)
![Corellation](https://github.com/Kriikle/Turnover_in_retail/blob/master/images/Correlation_matrix.png "Correlation matrix")

## So we go to making time sireis from the price * qty
After that, you need to prepare for viewing at the selected interval (t). And selected p,d,q for the arma model (arma if d = 0)
### Just for example Timesireies of tradeover for t = 7 days and arma(4,0)

Time sireis with MA:

![Time sireis](https://github.com/Kriikle/Turnover_in_retail/blob/master/images/Week_with_MA.png "Time siries")

Autocorelation:

![Autocorelation](https://github.com/Kriikle/Turnover_in_retail/blob/master/images/Week_autocorellation.png "Autocorelation")

adf:  -3.755792350369542

p-value:  0.0033934212624568832

Critical values:  {'1%': -3.4942202045135513, '5%': -2.889485291005291, '10%': -2.5816762131519275}
There are no unit roots, the series is stationary
![Time sireis](https://github.com/Kriikle/Turnover_in_retail/blob/master/images/Time_sireis_week.png "Forecosting")
