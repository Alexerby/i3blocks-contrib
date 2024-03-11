# i3blocks-yahoo

This is a script utilizing Yahoo Finance API to display the latest price in i3blocks.

## Configuration

```ini
[<label>]
label=<label>
instance=<label>
interval=<interval>
command=$SCRIPT_DIR/i3blocks-contrib/i3blocks-yahoo/latest.py <ticker>
```

### Example Nasdaq 100

```ini
[indice]
label=NDX100
instance=NDX
interval=60
command=$SCRIPT_DIR/i3blocks-contrib/i3blocks-yahoo/latest.py ^NDX
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
command=$SCRIPT_DIR/i3blocks-contrib/i3blocks-yahoo/latest.py BTC-USD

[crypto]
label=󰡪
color=#5F7AE3
separator=false
instance=ethereum
interval=60
command=$SCRIPT_DIR/i3blocks-contrib/i3blocks-yahoo/latest.py ETH-USD
separator_block_width=50
```

> Note that label icons may not be visible in this README markdown.

### Ticker
Find all tickers on Yahoo Finance [here](https://finance.yahoo.com/lookup/).

### Preview
![Selection_009](https://github.com/Alexerby/i3blocks-contrib/assets/57099109/c7b78073-c729-4f01-8120-1766ed5171cd)



