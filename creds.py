import random
import datetime
from google.cloud import datastore

def get_stubhub_key(project_id):
	return get_lru_key('Stubhub', project_id)
	
def get_email_key(project_id):
	return get_lru_key('Sendgrid', project_id)

###########################

# not used
#def get_random_key(project_id):
#	key_list = get_key_list(project_id)
#	return random.choice(key_list)

###########################

def get_lru_key(key_type, project_id):
	client = datastore.Client(project=project_id)
	query = client.query(kind='Creds')
	query.add_filter('key_type', '=', key_type)
	query.order = ['last_used']
	key_iter = query.fetch(1)
	for key in key_iter:
		key_to_return = key['key']
		key['last_used'] = datetime.datetime.utcnow()
		client.put(key)
	return key_to_return

#def get_key_list(project_id):
#	client = datastore.Client(project=project_id)
#	query = datastore.Query(client=client, kind='StubhubKey')
#	key_iter = query.fetch()
#	key_list = []
#	for key in key_iter:
#		key_list.append(key['key'])
#	return key_list

###########################
	
if __name__ == '__main__':
#	key_list = get_key_list('kochman-net-website')
#	print 'successfully retrieved ' + str(len(key_list)) + ' keys'
	print 'lru key: ' + get_stubhub_key('kochman-net-website')