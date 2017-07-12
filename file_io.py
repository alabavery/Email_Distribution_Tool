import json
import csv


def get_csv_addresses(csv_file_path):
	"""Read csv into variable and return it"""
	file = open(csv_file_path, 'r')
	reader_ = csv.reader(file)
	both_fields = []
	one_field_only = []

	for row in reader_:
		if row[1] == '1':
			if row[2] == '1':
				both_fields.append(row[0])
			else:
				one_field_only.append(row[0])

	file.close()
	return {'both_fields':both_fields, 'one_field_only':one_field_only}


def get_json_data(json_file_path):
	file = open(json_file_path, 'r')
	data = json.loads(file.read())
	file.close()
	return data


def write_json_data(json_file_path, data):
	data_json = json.dumps(data)
	json_file = open(json_file_path, 'w')
	json_file.write(data_json)
	json_file.close()


