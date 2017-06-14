import address_selection, file_io, gmail, tkinter_gui, config

SEEN_EMAIL_PATH = ""
ALL_ADDRESSES_PATH = ""
EXCEL_FILE_PATH = ""

gmail_client = gmail.get_gmail_client()

new_email_data = [('a',0),('b',0),('c',0)]

def main():
	gmail_client = get_gmail_client()
	unread_email_data = gmail.get_unread_email_data(gmail_client)
	
	seen_email_data = file_io.read_json_seen_email(seen_email_path)
	all_addresses = file_io.read_json_all_addresses(all_addresses_path)

	for email in new_email_data:
		d = address_selection.get_and_update_data_for_email(all_addresses, seen_email_data, email[0], email[1])
		gmail.send_email(d, email_address)



all_addresses = {'both_fields': list(range(200)), 'one_field_only': list(range(200,300))}
seen_email_data = []
postcard_indicator = 0
email_address = 'a'
d = address_selection.get_and_update_data_for_email(all_addresses, seen_email_data, email_address, postcard_indicator)
print(d)

# root = tkinter.Tk()
# gui = tkinter_gui.StartMenu(root, on_go_function, on_go_parameters)
# root.mainloop()
# root.destroy() # optional; see description below


	