# Networth Tracker
 
This project is created to keep track of user's net worth from their stock account from various exchanges.
Currently, I only found three libraries that I can use to pull data from three different exchange: 
 * Robinhood
 * TD Ameritrade
 * Gemini

First task of the project is to work on the data I got from Robinhood and try to draw a pie to represent the percentage of each stock that the user is holding.

To construct a pie chart, I will use a Matplotlib library.

The documentation for the library robin_stocks is: <br>
https://robin-stocks.readthedocs.io/en/latest/robinhood.html#sending-requests-to-api