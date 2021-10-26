# stocks-tracker
Python scripts to allow self-tracking of Investment Portfolio

<strong>Requirements</strong>:
1. Python 3.4 +
2. Pandas >= 0.23.1
3. Numpy >= 1.11.1
4. yfinance (To download market data from Yahoo Finance). You can read more about the package here (https://pypi.org/project/yfinance/)

## Quick Start
To start, clone the repo or download both python script from the 'script' folder

~~~
$ git clone https://github.com/Benlau93/stocks-tracker.git
~~~

You will also need the 'Transaction Data_template.xlsx' excel for it to work. The excel contains sheets with appropriate headers which the python script will populate.

### To add Transaction
<br>
Next, ensure that the excel sheet is in the same directory and rename the excel to 'Transaction Data.xlsx'. <br>
You can now start to populate the excel with your own investment transaction.
<br>
<br>
Open a powershell in the current folder and run 'Add_transaction.py' script
<br>

![command prompt](https://github.com/Benlau93/stocks-tracker/blob/main/img/quickstart_1.PNG?raw=true "Title")
<br>
The script will ask for details of the transaction in order to populate the correct stock
- DATE, format should be in DD-MM-YYYY (e.g. 23-10-2021)
- SYMBOL, symbol of the stock e.g. TSLA for Tesla or AAPL for Apple
- ACTION, allowable options are 'Buy' or 'Sell'
- PRICE, price at which the trade was executed
- SHARES, number of share transacted
- COMM, fees related to the transaction. Enter 0 if there is no fees
Enter these fields separated by a space
<br>

![command prompt2](https://github.com/Benlau93/stocks-tracker/blob/main/img/quickstart_2.PNG?raw=true "Title")
<br>
Press enter and the script will automatically populate the excel sheet <br>
<br>
Possible Scenarios:
1. No open position for symbol added, new open position will be added under 'Open' sheet
2. Symbol added has a current open position. If it is a 'Sell' ACTION, update the shares holding and close the position if 0 share left. Add the a close position under the 'Close' sheet
3. Symbol added has a current open position. If it is a 'Buy' ACTION, update the shares holding and the average buying price of the stock 

### To refresh stock price of open/existing positions
Open a powershell in the current folder and run 'refresh_stockprice.py' script
<br>

![command prompt3](https://github.com/Benlau93/stocks-tracker/blob/main/img/quickstart_3.PNG?raw=true "Title")
<br>
Automatically update the current prices for all exisitng position. Also, recalculate current value and P/L of the portfolio.

### Transaction Data Excel Sheet
Using the python scripts, the excel will be updated with all the transaction data and calculate fields such as P/L, P/L (%) that could be useful to track your trading performance.

The excel also allow easy ingestion into visualization softwares to monitor your trading progress. One example is shown below where I use the excel generated to create a simple dashboard to monitor my profits/loss on Tableau. <br>

![dashboard](https://github.com/Benlau93/stocks-tracker/blob/main/img/dashboard.PNG?raw=true "Title")

<br>
The interactive dashboard is also published on Tableau Public in the link here. (https://public.tableau.com/app/profile/benjamin.lau4995/viz/stock-tracker/Overview?publish=yes) 

##### Note
Shorting of Share is currently not supported in this version
