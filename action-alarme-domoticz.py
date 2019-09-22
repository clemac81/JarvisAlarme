#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author: Eric Vandecasteele 2018
# http://blog.onlinux.fr
#
#
# Import required Python libraries
import os
import requests
r = requests.get("http://192.168.1.38:8080/json.htm?type=command&param=switchlight&idx=119&switchcmd=On")
print(r.json)
