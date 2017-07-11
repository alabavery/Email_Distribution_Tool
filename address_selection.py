
def get_and_update_data_for_email(all_addresses, seen_email_data, email_address, attachment):
	"""
	all_addresses: dict of ['both_fields'] = [], ['one_field_only'] = []
	seen_email_data: list of {'email':'', 'both_fields': [], 'one_field_only': []}
	email_address: string email address
	attachment: bool True if email has attachment
	"""
	this_emails_seen_index = [i for i,email_data in enumerate(seen_email_data) if email_data['email'] == email_address]
	email_address_seen_before = len(this_emails_seen_index) == 1

	if email_address_seen_before and not attachment:
		print("Sender " + seen_email_data[this_emails_seen_index[0]] + " previously requested and has not included attachment.")
		return False

	else:
		selection = all_addresses['both_fields'][-10:]
		del all_addresses['both_fields'][-10:]

		if email_address_seen_before:
			seen_email_data[this_emails_seen_index[0]]['both_fields'].extend(selection)
		else:
			new_entry = {'email': email_address, 'one_field_only': [], 'both_fields': selection}
			seen_email_data.append(new_entry)

		return selection