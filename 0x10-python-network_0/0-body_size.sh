#!/bin/bash
# A bash scrip to print the size of body request
curl -w "%{size_download}\n" -o /dev/null -s $1
