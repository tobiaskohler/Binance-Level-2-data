# How to use



1. Install CRON jobs just like so

```
# websocket stream
5 21 * * * cd .../data_handler && ./websocket_controller.sh start >> .../data_handler/stream.log

# Orderbook Snapshot every 5 minutes
*/5 * * * * cd .../data_handler && ./snapshot_controller.sh start >> .../data_handler/stream.log
```
This will automatically start listening to the Binance websockets for 23 hours and 59 minutes. After that, it will stop, take a break and starts again 1 minute later.

The Orderbook snapshots will be taken automatically every 5 minutes as well.

2. In the case of special events and expected high volatility you are able to take manual snapshots in order to be able to replay the orderbook even in those "shaky" environments. For this do not call the shell script, but simply use the python script:
```
sudo python3 snapshot_handler.py
````


