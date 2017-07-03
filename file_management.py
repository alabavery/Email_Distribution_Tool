import os
import glob
import json


def get_csv_file_path(data_dir_path):
	"""Takes string, returns string"""
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

	return csv_file_list[0]


def get_json_file_path(data_dir_path, json_file_name):
	return os.path.join(data_dir_path, json_file_name)


def make_data_dir(data_dir_path, json_file_name, client_secret_file_name, client_secret):
	json_file = open(get_json_file_path(data_dir_path, json_file_name),'w')
	json_data = json.dumps([])
	json_file.write(json_data)
	json_file.close()

	json_file = open(get_json_file_path(data_dir_path, client_secret_file_name),'w')
	json_data = json.dumps(client_secret)
	json_file.write(json_data)
	json_file.close()


def ensure_data_dir_exists(data_dir_path, json_file_name):
	"""
	Takes string, no return
	More on logic -> 3rd answer at https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist
	"""
	try: 
	    os.makedirs(data_dir_path)
	    print("Created folder at " + data_dir_path)
	    make_data_dir(data_dir_path, json_file_name, client_secret_file_name, client_secret)

	except OSError: # will get OSError if the dir exists, if you don't have permissions, or other cases
	    if not os.path.isdir(data_dir_path): # only pay attention to the error if it is NOT due to the dir existing already
	        raise # make sure you know what happens if you don't have permissions so you can troubleshoot if that comes up
