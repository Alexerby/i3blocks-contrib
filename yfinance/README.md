# i3blocks-yahoo

This is a script utilizing Yahoo Finance API to display the latest price in i3blocks.

## Configuration
### Example Nasdaq 100
```ini
[indice]
label=NDX100
instance=NDX
interval=60
command=$SCRIPT_DIR/i3blocks-contrib/yfinance/latest ^NDX
separator_block_width=50
```

### Example BTC and ETH
```ini
[crypto]
label=󰠓 
color=#f7931a
separator=false
instance=bitcoin
interval=60
command=$SCRIPT_DIR/i3blocks-crypto/crypto
command=$SCRIPT_DIR/i3blocks-contrib/yfinance/latest BTC-USD

[crypto]
label=󰡪
color=#5F7AE3
separator=false
instance=ethereum
interval=60
command=$SCRIPT_DIR/i3blocks-contrib/yfinance/latest ETH-USD
separator_block_width=50
```

> Note that label icons may not be visible in this README markdown.

### Ticker
Find all tickers on Yahoo Finance [here](https://finance.yahoo.com/lookup/).

### Preview
![Selection_010](https://github.com/Alexerby/i3blocks-contrib/assets/57099109/55128866-d68e-4755-a0c7-e8270ded1abd)



