#!/bin/bash

# THIS SCRIPT IS USED TO START AND STOP BOTH THE WEBSOCKET STREAM
# IT IS MEANT TO BE RUN AS A CRON JOB FOR (24*60*60)- 60 SECONDS = 86340 SECONDS = 23.98 HOURS


websocket_lifetime=86340 #seconds

if [[ "$1" == "start" ]]; then

    echo "STARTED websocket_stream.sh AT $(date)"

    /usr/local/bin/python3 websocket_handler.py &
    
    sleep $websocket_lifetime

    pkill -9 -f websocket_handler.py


elif [[ "$1" == "stop" ]]; then

    echo "STOPPING websocket_stream.sh AT $(date)"

    # find the process ID of the snapshot_handler.py process
    pid=$(ps -ef | grep websocket_handler.py | grep -v grep | awk '{print $2}')

    if [[ -z "$pid" ]]; then
        echo "websocket_handler.py is not running"
    else
        # kill the process
        
        # loop over pid and kill all processes
        for i in $pid; do
        echo $i
            kill $i
        done
        

    fi
    
    echo "TERMINATED websocket_handler.py AT $(date)"

fi