#!/bin/bash
# Send GET request to the URL and capture response body
response=$(curl -s -o /dev/null -w "%{http_code}" "$1") [ "$response" = "200" ] && curl -s "$1"
