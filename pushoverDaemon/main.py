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
	print(url)

	secrets = None

	c.send_message("Daemon initializing...", title="duetBridge")

	last_percentage_sent = 0
	while True:
		try:
			response = requests.get(url)
			response = json.loads(response.text)

			status = response['status']
			if status != 'P':
				pass

			fraction_printed = int(response['fractionPrinted'])

			if fraction_printed > 0 and fraction_printed > last_percentage_sent and fraction_printed % threshold == 0:
				last_percentage_sent = fraction_printed
				c.send_message("Print is {}% complete".format(fraction_printed), title="duetBridge")
				
		except:
			pass

		sleep(interval)

if __name__ == '__main__':
	do_main()
