#!/bin/bash
# A bash script to print the methods allowed in a server
curl -s -i -X OPTIONS "$1" | grep "Allow:" | cut -d ":" -f2 | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//'
