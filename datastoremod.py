import datetime
from google.cloud import datastore

PROJECT_ID = 'kochman-net-website'


def write_ticket_price(price, event_id):
	client = datastore.Client()
	kind = 'TicketPrice'
	task_key = client.key(kind)
	task = datastore.Entity(key=task_key)
	task['price'] = float(price)
	task['event_id'] = int(event_id)
	task['datetime'] = datetime.datetime.utcnow()
	client.put(task)
	return
	
def get_event_dict():
	client = datastore.Client(project=PROJECT_ID)
	query = datastore.Query(client=client, kind='EventsToTrack')
	event_iter = query.fetch()
	event_dict = {}
	for event in event_iter:
		event_dict[event['event_id']] = event['target_price']
	return event_dict
	
def get_event_id():
	return get_event_dict().keys()[0]
