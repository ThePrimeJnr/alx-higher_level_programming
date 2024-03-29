#!/bin/bash
# Send GET request to the URL and capture response body

response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
if [ "$response" = "200" ]; then
	curl -s "$1"
fi
