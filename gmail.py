import httplib2
import os

from apiclient import discovery, errors
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from email.mime.text import MIMEText
import base64

import config


def get_credentials(data_dir_path, client_secret_file_path, scopes, application_name):
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    #home_dir = os.path.expanduser('~')
    #credential_dir = os.path.join(home_dir, '.credentials')
    credential_dir = os.path.join(data_dir_path, ".credentials")
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(client_secret_file_path, scopes)
        flow.user_agent = application_name

        try:
            import argparse
            flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        except ImportError:
            flags = None

        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def get_gmail_client(data_dir_path, client_secret_file_path, scopes, application_name):
    credentials = get_credentials(data_dir_path, client_secret_file_path, scopes, application_name)
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    return service


def get_unread_email_ids(gmail_client):
    """
    return list of id of unread emails
    """
    response = gmail_client.users().messages().list(userId='me',q='is:unread').execute()

    if 'messages' in response: # messages key only exists if there are unread messages
        return [message['id'] for message in response['messages']]
    else:
        print("No unread messages...")
        return [] # still return a list since that's what caller expects


def get_unread_email_data(gmail_client):
    """
    Use gmail api to find new emails
    Return email addresses of new emails and whether or not they have postcard
    """
    unread_ids = get_unread_email_ids(gmail_client)

    for message_id in unread_ids:
        remove_unread_label = {'removeLabelIds': ['UNREAD']}
        gmail_client.users().messages().modify(userId='me', id=message_id, body=remove_unread_label).execute()

        message_data = gmail_client.users().messages().get(userId='me',id=message_id).execute()
        message_payload = message_data['payload']
        has_attachment = 0 < len([part for part in message_payload['parts'] if part['mimeType'] == 'image/jpeg'])
        
        message_headers = message_payload['headers']
        sender = [header['value'] for header in message_headers if header['name'] == 'Return-Path'][0]
        yield sender, has_attachment



def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

    Returns:
    An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes())
    return {'raw':raw.decode()}


def send_message(message, client):
    """Send an email message.

    Args:
    client: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

    Returns:
    Sent Message.
    """
    try:
        message = (client.users().messages().send(userId='me', body=message).execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)


def send_addresses(sender, to, subject, addresses, intro_text, client):
    message_text = intro_text + '\n\n' + str(addresses)
    message = create_message(sender, to, subject, message_text)
    send_message(message, client)


def send_rejection(sender, to, subject, text, client):
    message = create_message(sender, to, subject, text)
    send_message(message, client)




def send_email(host_email, recipient_email, email_subject, email_body, gmail_client):
    message = create_message(host_email, recipient_email, email_subject, email_body)
    send_message(message, gmail_client)