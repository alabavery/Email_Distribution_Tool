import json

def read_excel(excel_file_path):
	"""
	check if it's been altered
	if so, read into and return variable
	if not, return None
	"""
	pass


def read_json_file(json_file_path):
	read_json = open(json_file_path, 'r').read()
	return json.loads(read_json)


def get_existing_data(excel_file_path, seen_email_file_path, all_addresses_file_path):
	updated_excel = read_excel(excel_file_path)
	
	if uptodate_excel:
		return updated_excel['all_addresses'], uptodate_excel['seen_email_']
	else:
		seen_email_data = read_json_file(seen_email_file_path)
		all_addresses = read_json_file(all_addresses_file_path)
		return {'seen_email_data':seen_email_data, 'all_addresses':all_addresses}
