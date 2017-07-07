
def get_and_update_data_for_email(all_addresses, seen_email_data, email_address):

	selection = all_addresses['both_fields'][:10]
	this_emails_seen_index = [i for i,email_data in enumerate(seen_email_data) if email_data['email'] == email_address]

	if len(this_emails_seen_index) == 1:
		seen_email_data[this_emails_seen_index[0]]['both_fields'].extend(selection)

	else:		
		new_entry = {'email': email_address, 'one_field_only': [], 'both_fields': selection}
		seen_email_data.append(new_entry)

	return selection