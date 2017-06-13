import address_selection, file_io, gmail



all_addresses = {'both_fields': list(range(200)), 'one_field_only': list(range(200,300))}
seen_email_data = []
postcard_indicator = 0
email_address = 'a'

"""
unread_emails = get_unread_emails()   -> this will be list of tuples, (email_address, postcard_indicator)
for email in unread_emails:
	selected_addresses = get_and_update_data_for_email(all_addresses, seen_email_data, email[0], email[1])
	send_addresses(selected_addresses, email[0])
"""


	