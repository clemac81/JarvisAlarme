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
import logging
import logging.config
from hermes_python.hermes import Hermes
from snipshelpers.config_parser import SnipsConfigParser

# Fixing utf-8 issues when sending Snips intents in French with accents
import sys
from SVT import SVT
from SVT import Constants

CONFIG_INI = "config.ini"
MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

# THERMOSTATSHIFT = 'ericvde31830:thermostatShift'
# THERMOSTATTURNOFF = 'ericvde31830:thermostatTurnOff'
# THERMOSTATMODE = 'ericvde31830:thermostatMode'

# os.path.realpath returns the canonical path of the specified filename,
# eliminating any symbolic links encountered in the path.
path = os.path.dirname(os.path.realpath(sys.argv[0]))
configPath = path + '/' + CONFIG_INI

logging.config.fileConfig(configPath)
logger = logging.getLogger(__name__)


def open_thermostat(config):
    # Set my own lan domoticz server ip address as default
    ip = config.get(
        'global', {
            "ip_domoticz": "192.168.1.38"}).get(
        'ip_domoticz', '192.168.1.38')
    # Set my own  domoticz server port as default : 8080
    port = config.get(
        'global', {
            "port": "8080"}).get(
        'port', '8080')
    # Initialize the all stuff
    thermostat = SVT(ip, port)

    logger.debug(" UrlBase domoticz:{}:{}".format(ip, port))
    logger.debug(" Indoor Temperature:{}°C".format(thermostat.indoorTemp))
    logger.debug(" Outdoor Temperature:{}°C".format(thermostat.outdoorTemp))
    logger.debug(" Thermostat Mode:{}".format(thermostat.mode))
    logger.debug(" Thermostat Pause:{}".format(thermostat.pause))
    logger.debug(" Thermostat State:{}".format(thermostat.state))
    logger.debug(" setpoint Day:  {}°C".format(thermostat.setpointNormal))
    logger.debug(" setpoint Night:{}°C".format(thermostat.setpointEconomy))
    return thermostat

r = requests.get("http://192.168.1.38:8080/json.htm?type=command&param=switchlight&idx=119&switchcmd=On")
print(r.text)

# def intent_received(hermes, intent_message):
   #  intentName = intent_message.intent.intent_name
   #  sentence = 'Voilà c\'est fait.'
   #  logger.debug(intentName)

    # for (slot_value, slot) in intent_message.slots.items():
       #  logger.debug('Slot {} -> \n\tRaw: {} \tValue: {}'
       #               .format(slot_value, slot[0].raw_value, slot[0].slot_value.value.value))

 

   #  if intentName == ACTIVATIONALARME:
     #    logger.debug("Thermostat turnOff")
     #    if intent_message.slots.activation:
       #      thermostat.state = 'stop'  # Turn economy mode on
       #      sentence = "Ok, je coupe le thermostat."
       #      logger.debug(sentence)
       #      hermes.publish_end_session(intent_message.session_id, sentence)
       #     return

   
          

# with Hermes(MQTT_ADDR) as h:

#     try:
 #        config = SnipsConfigParser.read_configuration_file(configPath)

 #    except BaseException:
 #        config = None

 #    thermostat = None

#     try:
#         thermostat = open_thermostat(config)
#         logger.info('Thermostat initialization: OK')

 #    except Exception as e:
 #        logger.error('Error Thermostat {}'.format(e))

  #   h.subscribe_intent(THERMOSTATMODE, intent_received)\
  #       .subscribe_intent(THERMOSTATTURNOFF, intent_received)\
  #       .subscribe_intent(THERMOSTATSHIFT, intent_received)\
  #       .start()
