import address_selection, file_io, gmail, tkinter_gui, config

SEEN_EMAIL_PATH = ""
ALL_ADDRESSES_PATH = ""
EXCEL_FILE_PATH = ""


all_addresses = {'both_fields': list(range(200)), 'one_field_only': list(range(200,300))}
seen_email_data = []
postcard_indicator = 0
email_address = 'a'


def main(excel_file_path, seen_email_file_path, all_addresses_file_path):
	existing_data = file_io.get_existing_data(excel_file_path, seen_email_file_path, all_addresses_file_path)
	gmail_client = gmail.get_gmail_client()
	unread_email_data = gmail.get_unread_email_data(gmail_client)

	for sender in unread_email_data:
		d = address_selection.get_and_update_data_for_email(all_addresses, seen_email_data, sender)
		print(d)
	# 	#gmail.send_email(d, email_address, gmail_client)



# root = tkinter.Tk()
# gui = tkinter_gui.StartMenu(root, on_go_function, on_go_parameters)
# root.mainloop()
# root.destroy() # optional; see description below


	