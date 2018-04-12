import sys
import time
import importlib
sh = importlib.import_module('stubhub_core')
emailmod = importlib.import_module('emailmod')
dsm = importlib.import_module('datastoremod')

PROJECT_ID = 'kochman-net-website'

def run_checks(argv):
	check_frequency = int(argv[1])
	last_price = {}
	while 1:
		event_dict = dsm.get_event_dict()
		for event in event_dict:
			event_id = event
			target_price = event_dict[event]
			try:
				result = sh.get_listings(event_id, '1', 0, 1)
				price = result['listing'][0]['currentPrice']['amount']
			except:
				f = open('output.txt', 'a')
				f.write('exception')
				f.close()
			else:
				if not (event_id in last_price):
					last_price[event_id] = -1
				if price != last_price[event_id]:
					last_price[event_id] = price
					if price <= target_price:
						email_result = emailmod.send_email('price now ' + str(price), 'body')
					dsm.write_ticket_price(price=price, event_id=event_id)
			time.sleep(check_frequency)
													

def old(argv):
	if len(argv) < 4:
		print 'Usage: python tixcount.py [check freq in seconds] [target price] [counter limit]'
	else:
		last_price = 0
		event_id = dsm.get_event_id()
		check_frequency = int(argv[1])
		target_price = int(argv[2])
		counter_limit = int(argv[3])
		counter = 0
		while 1:
			counter += 1
			try:
				result = sh.get_listings(event_id, '1', 0, 1)
				price = result['listing'][0]['currentPrice']['amount']
			except:
				f = open('output.txt', 'a')
				f.write('exception')
				f.close()
			else:
				if (price != last_price) or (counter >= counter_limit):
					if last_price != price:
						last_price = price				
						if price <= target_price:
							email_result = emailmod.send_email('price now ' + str(price), 'body')
					dsm.write_ticket_price(price=price, event_id=event_id)
					counter = 0
			time.sleep(check_frequency)

if __name__ == '__main__':
	run_checks(sys.argv)
		








