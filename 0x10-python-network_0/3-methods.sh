#!/bin/bash
# A bash script to print the methods allowed in a server
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
