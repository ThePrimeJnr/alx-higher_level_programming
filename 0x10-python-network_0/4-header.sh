#!/bin/bash
# A script that send get request to server with header X-School-User-Id = 98
curl -H "X-School-User-Id: 98" -sL $1
