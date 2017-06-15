#!CodeBlue/bin/python3.5
import address_selection, file_io, gmail, tkinter_gui

SEEN_EMAIL_PATH = "json/seen_email_data.json"
ALL_ADDRESSES_PATH = "json/all_addresses.json"
EXCEL_FILE_PATH = "demo_csv.csv"


def main(excel_file_path, seen_email_file_path, all_addresses_file_path):
	existing_data = file_io.get_existing_data(excel_file_path, seen_email_file_path, all_addresses_file_path)
	gmail_client = gmail.get_gmail_client()
	unread_email_data = gmail.get_unread_email_data(gmail_client)

	for sender in unread_email_data:
		d = address_selection.get_and_update_data_for_email(existing_data['all_addresses'], existing_data['seen_email_data'], sender)
		#gmail.send_email(d, gmail_client)

	file_io.write_json_file(existing_data['all_addresses'],all_addresses_file_path)
	file_io.write_json_file(existing_data['seen_email_data'],seen_email_file_path)


main(EXCEL_FILE_PATH, SEEN_EMAIL_PATH, ALL_ADDRESSES_PATH)
# root = tkinter.Tk()
# gui = tkinter_gui.StartMenu(root, on_go_function, on_go_parameters)
# root.mainloop()
# root.destroy() # optional; see description below


	