import json
import csv

def check_excel_altered(excel_file_path):
	return True


def read_excel(excel_file_path):
	"""
	check if it's been altered
	if so, read into and return variable
	if not, return None
	"""
	if not check_excel_altered(excel_file_path):
		return None
		
	else check_excel_altered(excel_file_path):
		file = open(excel_file_path, 'r')
		reader_ = csv.reader(file)
		both_fields = []
		one_field_only = []

		for row in reader_:
			if row[1] == '1':
				if row[2] == '1':
					both_fields_only.append(row[0])
				else:
					one_field_only.append(row[0])

		file.close()
		return {'both_fields':both_fields, 'one_field_only':one_field_only}


def write_json_file(data,json_file_path):
	j = json.dumps(data)
	file = open(json_file_path,'w')
	file.write(j)
	file.close()


def read_json_file(json_file_path):
	file = open(json_file_path, 'r')
	j = json.loads(file.read())
	file.close()
	return j


def get_existing_data(excel_file_path, seen_email_file_path, all_addresses_file_path):
	updated_excel = read_excel(excel_file_path)
	
	if updated_excel:
		return updated_excel['all_addresses'], uptodate_excel['seen_email_']
	else:
		seen_email_data = read_json_file(seen_email_file_path)
		all_addresses = read_json_file(all_addresses_file_path)
		return {'seen_email_data':seen_email_data, 'all_addresses':all_addresses}
