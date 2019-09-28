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

class SnipsConfigParser(ConfigParser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}


def sceneOn_received(hermes, intent_message):
	r = requests.get("http://192.168.1.38:8080/json.htm?type=command&param=switchlight&idx=119&switchcmd=On")
	print(r.json)
	hermes.publish_end_session(intent_message.session_id, "I'm sorry, I couldn't find a scene like "+lowest_name)

if __name__ == "__main__":
    global_conf = read_configuration_file(CONFIG_INI)
    domoticz_base_url = global_conf.get("secret").get("domoticz url")
    with Hermes('localhost:1883') as h:
        h.subscribe_intent("iMartyn:listScenes",listScenes_received) \
         .subscribe_intent("iMartyn:sceneOn",sceneOn_received) \
         .subscribe_intent("iMartyn:listSwitches",listSwitches_received) \
         .start()


