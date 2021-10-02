#!/usr/bin/env python3

import requests
import json
from time import sleep

import pushover

def get_secrets(filename='secrets.json'):
	with open(filename, 'rb') as f:
		return json.loads(f.read())

	return None

def do_main():
	secrets = get_secrets()

	pushover.init(secrets['token'])

	c = pushover.Client(secrets['user'])
	interval = secrets['interval']
	hostname = secrets['hostname']
	url = 'http://{}/rr_status?type=3'.format(hostname)
	threshold = secrets['threshold']

	secrets = None

	send_message = lambda msg : c.send_message(msg, title="duetBridge")

	send_message("Daemon intializing...")

	last_threshold_sent = 0
	while True:
		try:
			response = requests.get(url)
			response = json.loads(response.text)

			status = response['status']
			if status != 'P':
				if last_threshold_sent > 0:
					send_message("Print completed")
					last_threshold_sent = 0

			fraction_printed = int(response['fractionPrinted'])
			val = int(fraction_printed / threshold)

			if val > last_threshold_sent:
				last_threshold_sent = val
				send_message("Print is {}% complete".format(fraction_printed))
				
		except:
			pass

		sleep(interval)

if __name__ == '__main__':
	do_main()
