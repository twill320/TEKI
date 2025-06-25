import  yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import warnings
from mplfinance.original_flavor import candlestick_ohlc
from matplotlib import style
import mplfinance as mpf
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.ticker import FuncFormatter
from matplotlib import style

style.use('dark_background')

# handle y-axis values to present in scientific notation except values less than a certain amount
def sci_or_zero(x, pos):
    # x is the tick value
    if abs(x) < 1e-9:
        return "0"
    else:
        return f"{x:.2e}"

# filter FutureWarning
warnings.filterwarnings(
    "ignore",
    message=r".*YF\.download\(\).*auto_adjust.*",
    category=FutureWarning,
)

# graph sp500 data
def graph():
    # create figure, sublots
    fig = plt.figure(facecolor="black")
    ax1 = plt.subplot2grid((5, 1), (0, 0), rowspan=4, colspan=1)
    plt.title('S&P 500')
    plt.ylabel('OHLC(prices)', fontsize=12)
    ax2 = plt.subplot2grid((5, 1), (4, 0), rowspan=1, colspan=1, sharex=ax1)
    plt.ylabel('Volume(shares traded)', fontsize=12)

    # Fetch historical data for a specific period
    # You can use 'period' (e.g., "1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max") 
    # or 'start' and 'end' dates to specify the data range
    spfile = yf.download(
        "^GSPC",
        start="2024-08-01",
        end="2024-9-01",
        auto_adjust=False,
        progress=False
    )

    # replace index with standard indexes
    # creates extra column with previous index values
    spfile.reset_index(inplace=True)

    # build a float-date column just for plotting
    spfile['Date_num'] = mdates.date2num(spfile['Date'])

    # get ohlc data from sp500 download
    ohlc = spfile[['Date_num','Open','High','Low','Close']].astype(float).values
    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='red', colordown='green')
    
    # display grid for subplot 1
    ax1.grid(True)

    # plot bar graph with volume data
    ax2.bar(
       spfile['Date_num'].to_numpy(),
       spfile['Volume'].to_numpy().ravel(),
       width=1.0,
       align='center',
       color="#2596be",
       linewidth=0
    )

    # format dates
    ax2.xaxis_date()
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    
    # implement formatting large y-axis values to appear in scientific notation
    ax2.yaxis.set_major_formatter(FuncFormatter(sci_or_zero))

    # add slant to date values on x-axis
    fig.autofmt_xdate()

    # preset spacing of sublots
    plt.subplots_adjust(left=0.11, bottom=0.1, right=0.90,
                        top=0.90, wspace=0.4, hspace=0)
    # display grid for sublplot 2
    ax2.grid(True)

    plt.show()

    fig.savefig('sp500.png', facecolor=fig.get_facecolor())

if __name__ == "__main__":
    graph()
