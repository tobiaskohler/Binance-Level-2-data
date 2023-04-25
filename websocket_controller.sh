#!/bin/bash

# THIS SCRIPT IS USED TO START AND STOP BOTH THE WEBSOCKET STREAM
# IT IS MEANT TO BE RUN AS A CRON JOB FOR (24*60*60)- 60 SECONDS = 86340 SECONDS = 23.98 HOURS


websocket_lifetime=86340 #seconds

if [[ "$1" == "start" ]]; then

    echo "STARTED websocket_stream.sh AT $(date)"

    /usr/local/bin/python3 directory_handler.py &
    /usr/local/bin/python3 orderbook_updates_wss_handler.py &
    /usr/local/bin/python3 trade_wss_handler.py &

    sleep $websocket_lifetime

    echo "STOPPING all streams AT $(date)"

    # find the process ID of the snapshot_handler.py process
    pid_orderbook_updates=$(ps -ef | grep orderbook_updates_wss_handler.py | grep -v grep | awk '{print $2}')
    pid_trades=$(ps -ef | grep trade_wss_handler.py | grep -v grep | awk '{print $2}')

    if [[ -z "$pid_orderbook_updates" ]]; then
        echo "orderbook_updates_wss_handler.py is not running"
    else
        # kill the process
        
        # loop over pid and kill all processes
        for i in $pid_orderbook_updates; do
        echo $i
            kill $i
            echo "Killed $i (orderbook_updates_wss_handler.py)"
        done
        
    fi

        if [[ -z "$pid_trades" ]]; then
        echo "trade_wss_handler.py is not running"
    else
        # kill the process
        
        # loop over pid and kill all processes
        for i in $pid_trades; do
        echo $i
            kill $i
            echo "Killed $i (trade_wss_handler.py)"
        done
        

    fi
    
    echo "TERMINATED all running streams AT $(date)"


elif [[ "$1" == "stop" ]]; then

    echo "STOPPING all streams AT $(date)"

    # find the process ID of the snapshot_handler.py process
    pid_orderbook_updates=$(ps -ef | grep orderbook_updates_wss_handler.py | grep -v grep | awk '{print $2}')
    pid_trades=$(ps -ef | grep trade_wss_handler.py | grep -v grep | awk '{print $2}')

    if [[ -z "$pid_orderbook_updates" ]]; then
        echo "orderbook_updates_wss_handler.py is not running"
    else
        # kill the process
        
        # loop over pid and kill all processes
        for i in $pid_orderbook_updates; do
        echo $i
            kill $i
            echo "Killed $i (orderbook_updates_wss_handler.py)"
        done
        

    fi

        if [[ -z "$pid_trades" ]]; then
        echo "trade_wss_handler.py is not running"
    else
        # kill the process
        
        # loop over pid and kill all processes
        for i in $pid_trades; do
        echo $i
            kill $i
            echo "Killed $i (trade_wss_handler.py)"
        done
        

    fi
    
    echo "TERMINATED all running streams AT $(date)"

fi