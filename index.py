import os

import file_management
import file_io
import address_selection
import gmail
import config


base_path = os.path.dirname(os.path.realpath(__file__))
data_dir_path = os.path.join(base_path, config.DATA_DIR_NAME)
seen_email_file_path = os.path.join(data_dir_path, config.SEEN_EMAIL_FILE_NAME)
address_json_file_path = os.path.join(data_dir_path, config.ADDRESSES_JSON_FILE_NAME)
client_secret_file_path = os.path.join(data_dir_path, config.CLIENT_SECRET_FILE_NAME)
client_secret = config.CLIENT_SECRET

# looks for data dir, ensures it contains csv, creates dir and prompts user for csv if not found, then copies rest of necessary data
file_management.ensure_data_exists(data_dir_path, 
									address_json_file_path, 
									seen_email_file_path, 
									client_secret_file_path, 
									client_secret)

# WARNING:::: three lines below assume that csv file WILL NOT CHANGE after initial saving
all_addresses = file_io.get_json_data(address_json_file_path)
used_addresses = all_addresses['used']
unused_addresses = all_addresses['unused']

seen_email_data = file_io.get_json_data(seen_email_file_path)
gmail_client = gmail.get_gmail_client(data_dir_path, client_secret_file_path, config.SCOPES, config.APPLICATION_NAME)
new_email_data = gmail.get_unread_email_data(gmail_client)

for email in new_email_data:
	addresses_to_send = address_selection.get_and_update_data_for_email(unused_addresses, 
																		used_addresses, 
																		seen_email_data, 
																		email[0], # sender address
																		email[1]) # attachment bool var

	if addresses_to_send: # will be false if sender who has been seen before but did not send attachment
 		gmail.send_addresses(config.APPLICATION_EMAIL, email[0], config.SUBJECT, addresses_to_send, config.INTRO_TEXT, gmail_client)
	else:
		gmail.send_rejection(config.APPLICATION_EMAIL, email[0], config.REJECTION_SUBJECT, config.REJECTION_TEXT, gmail_client)

new_all_addresses = {'used': used_addresses, 'unused': unused_addresses}
file_io.write_json_data(address_json_file_path, new_all_addresses)
file_io.write_json_data(seen_email_file_path, seen_email_data)


