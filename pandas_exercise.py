# This is a code for exercises for pandas lecture.

# Nurullah Gulec 5 August 2020

# First Exercise
import pandas as pd
import datetime as dt
from pandas_datareader import data
from matplotlib import pyplot as plt


ticker_list = {'INTC': 'Intel',
                        'MSFT': 'Microsoft',
                        'IBM': 'IBM',
                        'BHP': 'BHP',
                        'TM': 'Toyota',
                        'AAPL': 'Apple',
                        'AMZN': 'Amazon',
                        'BA': 'Boeing',
                        'QCOM': 'Qualcomm',
                        'KO': 'Coca-Cola',
                        'GOOG': 'Google',
                        'SNE': 'Sony',
                        'PTR': 'PetroChina'}

def read_data(ticker_list, start,
                   end):
    """
    This function reads in closing price data from Yahoo for each tick in the ticker_list.
    """
    ticker = pd.DataFrame()
    for tick in ticker_list:
        prices = data.DataReader(tick, 'yahoo', start, end)
        closing_prices = prices['Close']
        ticker[tick] = closing_prices
    return ticker

start=dt.datetime(2019, 1, 2)
end=dt.datetime(2019, 12, 31)
ticker = read_data(ticker_list, start, end)


p0=ticker.iloc[0]
p1=ticker.iloc[-1]


growth= 100* (p1-p0)/p0


growth.columns=['stock','change']
print(growth)

growth.sort_values(inplace=True)

growth = growth.rename(index=ticker_list)
fig, ax = plt.subplots(figsize=(10,8))
ax.set_xlabel('stock', fontsize=12)
ax.set_ylabel('percentage change in price', fontsize=12)
growth.plot(kind='bar', ax=ax)
plt.show()



################################################################################################
# Second Exercise

indices_list = {'^GSPC': 'S&P 500' , '^IXIC': 'NASDAQ','^DJI': 'Dow Jones',
                '^N225': 'Nikkei'}

start=dt.datetime(1928, 1, 2)
end=dt.datetime(2020, 7, 31)

ticker2= read_data(indices_list, start, end)

ticker2.describe()

yearly_returns= pd.DataFrame()
for index, name in indices_list.items():
    p1=ticker2.groupby(ticker2.index.year)[index].first() # First data on the year/
    p2=ticker2.groupby(ticker2.index.year)[index].last()  #Second data on the year.
    returns= (p2-p1)/p1
    yearly_returns[name]=returns
yearly_returns

yearly_returns.describe()


fig, axes = plt.subplots(2, 2, figsize=(10, 6))

for iter, ax in enumerate(axes.flatten()):
    index_name=yearly_returns.columns[iter]
    ax.set_title(indexname)
    ax.set_ylabel('Percent Change', fontsize=12)
    ax.plot(yearly_returns[index_name])

plt.tight_layout()