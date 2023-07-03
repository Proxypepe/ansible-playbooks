#!/bin/bash
# WANT_JSON

host=`jq -r .host < $1`
port=`jq -r .port < $1`
timeout=`jq -r .timeout < $1`

if [[ $timeout = null ]]; then
    timeout=3
fi 

nc -z -w $timeout $host $port

if [ $? -eq 0 ]; then
    echo '{"changed": false, "msg": "Reached"}'
else
    echo "{\"failed\": true, \"msg\": \"could not reach $host:$port\"}"
fi