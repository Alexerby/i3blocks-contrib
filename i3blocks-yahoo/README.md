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

Example Nasdaq 100

```ini
[indice]
label=NDX100
instance=NDX
interval=60
command=$SCRIPT_DIR/i3blocks-contrib/i3blocks-yahoo/latest.py ^NDX
```

## Ticker
Find all tickerson Yahoo Finance [here](https://finance.yahoo.com/lookup/).
