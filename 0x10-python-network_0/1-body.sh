#!/bin/bash
# Send GET request to the URL and capture response body
response=$(curl -s -o /dev/null -w "%{http_code}" -L "$1"); [ "$response" = "200" ] && curl -s -L "$1"
