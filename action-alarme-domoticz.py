#!/usr/bin/env python3
# Import required Python libraries
import requests
r = requests.get("http://192.168.1.38:8080/json.htm?type=command&param=switchlight&idx=119&switchcmd=On")
print(r.json)
