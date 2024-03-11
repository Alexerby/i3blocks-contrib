#!/usr/bin/env python3
# coding=utf-8

import yfinance as yf
import sys

PRICE_CHANGE_PERIOD = '1d'  # You can adjust this period as needed

def get_ticker(ticker):
    try:
        # Fetch data
        data = yf.Ticker(ticker)
        
        # Get current index value and opening price
        current_index = data.history(period=PRICE_CHANGE_PERIOD)["Close"].iloc[-1]
        open_price = data.history(period=PRICE_CHANGE_PERIOD)["Open"].iloc[-1]
        
        # Calculate the percentage change
        percent_change = ((current_index - open_price) / open_price) * 100
        
        return current_index, percent_change
    except Exception as e:
        print("Error fetching data:", e)
        return None, None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <ticker>")
        sys.exit(1)
    
    ticker = sys.argv[1]
    index_value, percent_change = get_ticker(ticker)
    if index_value is not None and percent_change is not None:
        # Determine the color and icon based on the percentage change
        color = '#3BB92D' if percent_change > 0 else '#F7555E'
        icon = '🠕' if percent_change > 0 else '🠗'
        

        print(('{:.2f} <span color="{}">{} {:.2f}%</span>').format(index_value, color, icon, percent_change))
        

