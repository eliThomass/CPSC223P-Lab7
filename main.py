import contacts

exit_program = False
contacts = contacts.Contacts('filename.dat')

while not exit_program:
	print("\n      *** TUFFY TITAN CONTACT MAIN MENU\n")
	print("1. Add contact")
	print("2. Modify contact")
	print("3. Delete contact")
	print("4. Print contact list")
	print("5. Set contact filename\n")
	choice = input("Enter menu choice: ")
	print("\n")
	if choice == '1':
		phone = input("Enter phone number: ")
		first = input("Enter first name: ")
		last = input("Enter last name: ")
		contacts.add_contact(phone, first, last)
	if choice == '2':
		phone = input("Enter phone number: ")
		first = input("Enter first name: ")
		last = input("Enter last name: ")
		contacts.modify_contact(phone, first, last)
	if choice == '3':
		phone = input("Enter phone number: ")
		contacts.delete_contact(phone)
	if choice == '4':
		print("==================== CONTACT LIST ====================")
		print("Last Name             First Name            Phone")
		print("====================  ====================  ==========")
		print(contacts.print_contacts())
	if choice == '5':
		filename = input("Set filename: ")
		contacts.__init__(filename)
	if choice == '6':
		exit_program = True
	
