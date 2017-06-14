import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def get_gmail_client():
	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('gmail', 'v1', http=http)
	return service


def get_unread_email_ids(gmail_client):
	"""
	return list of id of unread emails
	"""
	response = gmail_client.users().messages().list(userId='me',q='is:unread').execute()
	ids = [message['id'] for message in response['messages']]
	return ids


def get_unread_email_data(gmail_client):
	"""
	Use gmail api to find new emails
	Return email addresses of new emails and whether or not they have postcard
	"""
	unread_ids = get_unread_email_ids(gmail_client)

	for message_id in unread_ids:
		message_data = gmail_client.users().messages().get(userId='me',id=message_id).execute()
		message_headers = message_data['payload']['headers']
		sender = [header['value'] for header in message_headers if header['name'] == 'Return-Path'][0]
		yield sender


def send_email(recipient_email, email_subject, email_body, host_email_address, host_email_password):
	pass