import  pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
def main() :
    data=load_dataset("TSLA_stock_data.csv")
    moving_averages(data)
    candlestick_chart(data)
    daily_returns(data)
# 📈 Function 1: Calculate and plot 20-day and 50-day moving averages
def moving_averages(data):
    # Calculate 20-day and 50-day moving averages

    data['MA_20'] = data['Close'].rolling(window=20).mean()
    data['MA_50'] = data['Close'].rolling(window=50).mean()
    
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['MA_20'], label='20-Day MA', color='orange')
    plt.plot(data['MA_50'], label='50-Day MA', color='red')
    plt.title("TESLA Stock Price with Moving Averages")
    plt.legend()
    plt.grid()
    plt.savefig("moving_averages.png")
    plt.show()

# 🕯️ Function 2: Create a candlestick chart from OHLC data
def candlestick_chart(data):
    # Prepare data
    df_plot = data.reset_index()[['Date', 'Open', 'High', 'Low', 'Close']]
    df_plot['Date'] = pd.to_datetime(df_plot['Date'])
    df_plot['Date'] = df_plot['Date'].map(mdates.date2num)

    # Plot
    fig, ax = plt.subplots(figsize=(15, 7))
    candlestick_ohlc(ax, df_plot.values, width=1.7, colorup='green', colordown='red')
    ax.xaxis_date()
    plt.title("TESLA Candlestick Chart (2023)")
    plt.xlabel("Date")
    plt.ylabel("Price ($)")
    plt.grid()
    plt.savefig("candlestick.png")
    plt.show()
# 📊 Function 3: Calculate and plot daily return (volatility)
def daily_returns(data):
    data['Daily_Return'] = data['Close'].pct_change() * 100
    plt.figure(figsize=(12, 4))
    plt.plot(data['Daily_Return'], label='Daily Returns', color='purple')
    plt.title("TESLA  Daily Volatility")
    plt.axhline(0, color='black', linestyle='--')
    plt.grid()
    plt.savefig("volatility.png")
    plt.show()

def load_dataset (file_path):
    """Load dataset from CSV file and perform initial data inspection.

        Args:
            file_path (str): Path to the CSV file

        Returns:
            DataFrame: Loaded dataset or None if file not found
        """
    try :
        ds=pd.read_csv(file_path)
        print("Missing Values : \n" ,ds.isnull().sum())
        print ("\nSummary state : \n",ds.describe())
        return ds
    except :
        TypeError("file isn't exist")
        return None

if __name__ =="__main__" :
    main()