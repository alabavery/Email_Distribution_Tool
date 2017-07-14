import os
import glob
import json

import file_io

def prompt_user_to_save_csv(data_dir_path):
	# no return
	csv_file_list = []
	while True:
		csv_file_list = glob.glob(data_dir_path + '/*.csv')
		if len(csv_file_list) > 0:
			break
		print()
		print("..........................................................")
		print("CSV data file not found at " + data_dir_path + "/")
		print("Please save file as a '.csv' to " + data_dir_path + "/ before continuing.")
		input("Press ENTER when you have saved the file...")


def get_csv_file_path(data_dir_path):
	# must be sure that this will not be run before success of prompt_user_to_save_csv()
	return glob.glob(data_dir_path + '/*.csv')[0]


def copy_csv_to_all_addresses_json_file(all_addresses_file_path):
	csv_file_path = get_csv_file_path(data_dir_path)
	csv_addresses = file_io.get_csv_addresses(csv_file_path)
	all_addresses = {'used': {'both_fields': [], 'one_field_only': []}, 'unused': csv_addresses}
	file_io.write_json_data(all_addresses_file_path, all_addresses)


def fill_data_dir(data_dir_path, 
				all_addresses_file_name, 
				seen_email_file_name, 
				client_secret_file_name, 
				client_secret):
	prompt_user_to_save_csv(data_dir_path)
	copy_csv_to_all_addresses_json_file(os.path.join(data_dir_path, all_addresses_file_name))
	file_io.write_json_data(seen_email_file_path, []) # make seen email file containing only empty list json
	file_io.write_json_data(client_secret_file_path, client_secret)


def ensure_data_exists(data_dir_path, all_addresses_file_name, seen_email_file_name, client_secret_file_name, client_secret):
	"""
	Takes string, no return
	More on logic -> 3rd answer at https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist
	"""
	try: 
	    os.makedirs(data_dir_path)
	    print("Created folder at " + data_dir_path)
	   	fill_data_dir(data_dir_path, all_addresses_file_name, seen_email_file_name, client_secret_file_name, client_secret)

	except OSError: # will get OSError if the dir exists, if you don't have permissions, or other cases
	    if not os.path.isdir(data_dir_path): # only pay attention to the error if it is NOT due to the dir existing already
	        raise # make sure you know what happens if you don't have permissions so you can troubleshoot if that comes up
