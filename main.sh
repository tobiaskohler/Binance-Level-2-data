#!/bin/bash

# THIS SCRIPT IS USED TO START AND STOP BOTH THE WEBSOCKET STREAM AND THE SNAPSHOT HANDLER 
# IT IS MEANT TO BE RUN AS A CRON JOB FOR (24*60*60)- 60 SECONDS = 86340 SECONDS = 23.98 HOURS


if [[ "$1" == "start" ]]; then

    echo "STARTED main.sh AT $(date)"

    /usr/local/bin/python3 websocket_handler.py &

    while true; do
        /usr/local/bin/python3 snapshot_handler.py &
        sleep 30
        pkill -f snapshot_handler.py
    done

    pkill -f websocket_handler.py


elif [[ "$1" == "stop" ]]; then

    pkill -9 -f websocket_handler.py
    pkill -9 -f snapshot_handler.py

    echo "TERMINATED main.sh AT $(date)"

fi