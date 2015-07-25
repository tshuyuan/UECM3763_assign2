from pandas.io.data import DataReader as DR
from datetime import datetime as dt

#The collection of data starting from 17/7/2010 to 16/7/2015
start = dt(2010, 7, 17)
end = dt(2015, 7, 16)

#Public Bank Berhad with stock code: 1295.KL is chosen
#Closing price is obtained
pbe_closing = DR("1295.KL", 'yahoo', start, end)['Close']
#To define a function that is use to calculate the moving average
import numpy as np
def moving_average(values, days):
    weights = np.repeat(1.0, days)/days
    sma = np.convolve(values, weights, 'valid')
    return sma
#To calculate the 5 days moving average
MovingAverageX5 = moving_average(pbe_closing, 5)    
#To plot the moving average
import matplotlib.pyplot as plt
count = len(MovingAverageX5)
xaxis = np.arange(count) + 5
yaxis = MovingAverageX5
plt.xlabel('Day $n$')
plt.ylabel('Moving Average (MYR)')
plt.plot(xaxis,yaxis)
plt.title('Plot of 5-day Moving Average')

print(' ')
print('FTSEKLCI component chosen: PUBLIC BANK BERHAD (1295.KL)')
plt.show()


#1295.KL and ^KLSE is the stock code for Public Bank berhad and KLSE respectively
symbols = ['1295.KL', '^KLSE']
#To download the closing data of Public Bank Berhad and KLSE
pbe_klse_closing = DR(symbols, 'yahoo', start, end)['Close']
#To find the correlation of Public Bank Berhad and KLSE
correlation = pbe_klse_closing.corr()

print(' ')
print('The correlation of FTSEKLCI and Public Bank Berhad is as following:')
print(correlation)
print(' ')