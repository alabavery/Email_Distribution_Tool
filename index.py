import os

import file_management
import file_io
import address_selection
import gmail
import config


base_path = os.path.dirname(os.path.realpath(__file__))
data_dir_path = os.path.join(base_path, config.DATA_DIR_NAME)
seen_email_file_path = os.path.join(data_dir_path, config.SEEN_EMAIL_FILE_NAME)
client_secret_file_path = os.path.join(data_dir_path, config.CLIENT_SECRET_FILE_NAME)
client_secret = config.CLIENT_SECRET

file_management.ensure_data_exists(data_dir_path, config.SEEN_EMAIL_FILE_NAME, config.CLIENT_SECRET_FILE_NAME, config.CLIENT_SECRET)
csv_file_path = file_management.get_csv_file_path(data_dir_path)

all_addresses = file_io.get_csv_addresses(csv_file_path)
both_fields_addresses = all_addresses['both_fields']
one_field_addresses = all_addresses['one_field_only']
seen_email_data = file_io.get_seen_email_data(seen_email_file_path)


new_email_data = [('a',1),('b',0),('c',0),('d',0)]
for email in new_email_data:
	print(address_selection.get_and_update_data_for_email(all_addresses, seen_email_data, email[0]))

file_io.write_seen_email_data(seen_email_file_path, seen_email_data)


