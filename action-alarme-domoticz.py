#!/usr/bin/env python2
from hermes_python.hermes import Hermes
from datetime import datetime
from pytz import timezone
import requests

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def intent_received(hermes, intent_message):

	print()
	print(intent_message.intent.intent_name)
	print ()

	if intent_message.intent.intent_name == 'Clemac81:ActivationAlarme':
        r = requests.get("http://192.168.1.38:8080/json.htm?type=command&param=switchlight&idx=119&switchcmd=On")
        print(r.json)
		

		# hermes.publish_continue_session(intent_message.session_id, sentence, ["Joseph:greetings"])
		hermes.publish_end_session(intent_message.session_id, sentence)




with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()

#if intentName == 
#r = requests.get("http://192.168.1.38:8080/json.htm?type=command&param=switchlight&idx=119&switchcmd=On")
#    print(r.json)
#current_session_id = intentMessage.session_id
#hermes.publish_end_session(current_session_id, result_sentence)

