#!/bin/bash

# THIS SCRIPT IS USED TO START AND STOP THE SNAPSHOT HANDLER 

snapshot_interval=300 # every 5 minutes seconds

if [[ "$1" == "start" ]]; then

    echo "STARTED snapshot_controller.sh AT $(date)" &

    while true; do
        /usr/local/bin/python3 snapshot_handler.py &
        sleep $snapshot_interval
    done


elif [[ "$1" == "stop" ]]; then

    echo "STOPPING snapshot_controller.sh AT $(date)"

    # find the process ID of the snapshot_handler.py process
    pid=$(ps -ef | grep snapshot_controller.sh | grep -v grep | awk '{print $2}')

    if [[ -z "$pid" ]]; then
        echo "snapshot_controller.sh is not running"

    else
        # kill the process
        
        # loop over pid and kill all processes
        for i in $pid; do
        echo $i
            kill $i
        done
    
    
    fi
        
    echo "TERMINATED snapshot_controller.sh AT $(date)"

    else

        echo "Invalid argument: $1"
        echo "Usage: $0 [start|stop]"


fi