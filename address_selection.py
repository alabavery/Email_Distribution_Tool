
def select_addresses(candidates, black_list):
	selection = []

	for candidate in candidates:

		if len(selection) > 9:
			return selection

		if candidate not in black_list:
			selection.append(candidate)

	return selection


def get_and_update_data_for_email(all_addresses, seen_email_data, email_address, postcard_indicator):

	this_emails_seen_index = [i for i,email_data in enumerate(seen_email_data) if email_data['email'] == email_address]

	if len(this_emails_seen_index) == 1:
		this_emails_seen_data = seen_email_data[this_emails_seen_index[0]]
		selection = select_addresses(all_addresses['both_fields'], this_emails_seen_data['both_fields'])
		seen_email_data[this_emails_seen_index[0]]['both_fields'].extend(selection)

		if len(selection) < 10:
			one_field_selection = select_addresses(all_addresses['one_field_only'], this_emails_seen_data['one_field_only'])
			seen_email_data[this_emails_seen_index[0]]['one_field_only'].extend(one_field_selection)
			selection.extend(one_field_selection)
	else:
		selection = all_addresses['both_fields'][:10]
		new_entry = {'email': email_address, 'one_field_only': [], 'both_fields': selection}
		seen_email_data.append(new_entry)

	return selection