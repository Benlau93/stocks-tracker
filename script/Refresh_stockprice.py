import pandas as pd
import yfinance as yf
from datetime import date

def main():
    df = pd.read_excel("Transaction Data.xlsx",sheet_name=None)
    data = df["Data"]
    open_ = df["Open Position"]
    closed = df["Closed Position"]
    # convert datetime
    open_["Date"] = pd.to_datetime(open_["Date"],format ="%Y-%m-%d")
    
    for sym in open_["Symbol"].unique():
        idx = open_[open_["Symbol"]==sym].index[0]
        ticker = sym
            
        # get stock price
        history = yf.download(tickers=ticker,period="3d")
        open_.loc[idx,"Previous Close"] = history["Close"].iloc[-1]
        open_.loc[idx,"% Change"] = ((history["Close"].iloc[-1] - history["Close"].iloc[-2])/history["Close"].iloc[-2])
        open_.loc[idx,"Change"] = history["Close"].iloc[-1] - history["Close"].iloc[-2]
    
    	# get current P/L
        open_.loc[idx,"P/L"] = round((history["Close"].iloc[-1] * open_.loc[idx,"Shares"])  - (open_.loc[idx,"Avg Price"] * open_.loc[idx,"Shares"] + open_.loc[idx,"Comm"]),2)    	    
        open_.loc[idx,"P/L (%)"] = open_.loc[idx,"P/L"] / open_.loc[idx,"Amount"]
        
        # generate current value of stock
        open_.loc[idx,"Value"] = open_.loc[idx,"Previous Close"] * open_.loc[idx,"Shares"]
        print("Sucessfully update price for {}".format(sym))

        # get number of holdings
        open_.loc[idx,"Holdings (days)"] = (pd.to_datetime(date.today()) - open_.loc[idx,"Date"]).days
    


    # generate new weightage
    open_["Weightage"] = open_["Value"] / open_["Value"].sum()
    
    # write to excel
    with pd.ExcelWriter("Transaction Data.xlsx",
    	                    date_format="DD-MMM-YY",
    	                    datetime_format = "DD-MMM-YY") as writer:
        data.to_excel(writer,sheet_name="Data",index=False)
        closed.to_excel(writer,sheet_name="Closed Position",index=False)
        open_.to_excel(writer,sheet_name="Open Position",index=False)
        
if __name__== "__main__":
  main()

