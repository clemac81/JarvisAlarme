#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import ConfigParser
import urllib2
import json
import io
import jellyfish
from hermes_python.hermes import Hermes
import configparser
from hermes_python.ffi.utils import MqttOptions
from hermes_python.ontology import *
import io
import requests


CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"
MAX_JARO_DISTANCE = 0.4

if intentName == 'Clemac81:ActivationAlarme':
    r = requests.get("http://192.168.1.38:8080/json.htm?type=command&param=switchlight&idx=119&switchcmd=On")
    print(r.json)
current_session_id = intentMessage.session_id
hermes.publish_end_session(current_session_id, result_sentence)

