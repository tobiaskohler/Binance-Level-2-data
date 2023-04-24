#!/bin/bash

if [[ "$1" == "start" ]]; then
    /usr/bin/python3 websocket_handler.py &
    /usr/bin/python3 snapshot_handler.py &
    sleep 60
    pkill -f websocket_handler.py

# Stop all processes
elif [[ "$1" == "stop" ]]; then
    pkill -f websocket_handler.py
    pkill -f snapshot_handler.py
    
fi
