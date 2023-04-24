#!/bin/bash

# THIS SCRIPT IS USED TO START AND STOP BOTH THE WEBSOCKET STREAM
# IT IS MEANT TO BE RUN AS A CRON JOB FOR (24*60*60)- 60 SECONDS = 86340 SECONDS = 23.98 HOURS


#websocket_lifetime=86340 #seconds
websocket_lifetime=120 #seconds

if [[ "$1" == "start" ]]; then

    echo "STARTED websocket_stream.sh AT $(date)"

    /usr/local/bin/python3 websocket_handler.py &
    
    sleep $websocket_lifetime

    pkill -9 -f websocket_handler.py


elif [[ "$1" == "stop" ]]; then
    echo "TERMINATED websocket_stream.sh AT $(date)"

    pkill -9 -f websocket_handler.py

fi