import matplotlib_inline
import yfinance as yf
import pandas as pd
# Using the `Ticker` module we can create an object that will allow us to access functions to extract data. To do this we need to provide the ticker symbol for the stock, here the company is Apple and the ticker symbol is `AAPL`.
apple = yf.Ticker("AAPL")
print("Ticker Object:",apple)
# print(apple.info)
# print(apple.history(period="max"))
import os
file_path = os.path.join(os.path.dirname(__file__), 'apple.json')
print(file_path)
import json
with open(file_path,"r") as json_file:
    apple_info = json.load(json_file)
print(type(apple_info))
# print(apple_info["website"])
# Example
amd= yf.Ticker("AMD")
amd_share_price=amd.history(period="max").head(1)
print(amd_share_price[["Volume"]])
