import requests
import importlib
creds = importlib.import_module('creds')

PROJECT_ID = 'kochman-net-website'

def get_email_content(subject, body):
	out =  '''
        {
  "personalizations": [
    {
      "to": [
        {
          "email": "rkochman@gmail.com"
        },
        {
          "email": "4258909448@txt.att.net"
      	}
      ],
      "subject": "'''
	out += subject
	out += '''"
    }
  ],
  "from": {
    "email": "rkochman@gmail.com"
  },
  "content": [
    {
      "type": "text/plain",
      "value": "'''
	out += body
	out += '''"
    }
  ]
}
'''
	return out
	
def get_email_token():
	return creds.get_email_key(PROJECT_ID)

def send_email(subject, body):
	email_content = get_email_content(subject, body)
	email_url = 'https://api.sendgrid.com/v3/mail/send'
	email_headers = {'Authorization': get_email_token(), 
		'Content-Type': 'application/json',
		'Access-Control-Allow-Origin': '*'} 
	email_result = requests.post(email_url, headers=email_headers, data=email_content)
	return email_result
	
if __name__ == '__main__':
	result = send_email('Test Subject', 'Test Body')
	print result