import json

class Contacts:
	
	def __init__(self, filename):
		self.name = filename
		self.contact_dict = {}
		try:
			with open(filename, 'r') as f:
				self.contact_dict = json.load(f)
		except FileNotFoundError:
			print("File not found.")
		except Exception as e:
			print(f"Unexpected error: {e}")
			
	def add_contact(self, id, first_name, last_name):
		if id in self.contact_dict.keys():
			print("Phone number already exists.")
			return "error"
		if id.isnumeric() == False:
			print("Invalid phone number")
			return "error"
		fullname = [first_name, last_name]
		self.contact_dict[id] = fullname
		self.contact_dict = dict(sorted(self.contact_dict.items(), key=lambda item: item[1]))
		try:
			with open(self.name, 'w') as f:
				json.dump(self.contact_dict,f)
				print(f"Added: {first_name} {last_name}.")
		except Exception as e:
			print(f"Unexpected error: {e}")
		return f'{id} : {self.contact_dict[id]}'
		
	def modify_contact(self, id, first_name, last_name):
		if id not in self.contact_dict.keys():
			print("Invalid phone number.")
			return "error"
		self.contact_dict.pop(id)
		self.contact_dict[id] = [first_name, last_name]
		self.contact_dict = dict(sorted(self.contact_dict.items(), key=lambda item: item[1]))
		try:
			with open(self.name, 'w') as f:
				json.dump(self.contact_dict,f)
				print(f"Modified: {first} {last}.")
		except Exception as e:
			print(f"Unexpected error: {e}")
		return f'{id} : {self.contact_dict[id]}'
		
	def delete_contact(self, id):
		if id not in self.contact_dict.keys():
			print("Invalid phone number.")
			return "error"
		return_name = self.contact_dict[id]
		self.contact_dict.pop(id)
		try:
			with open(self.name, 'w') as f:
				json.dump(self.contact_dict,f)
				print(f"Deleted: {phone}.")
		except Exception as e:
			print(f"Unexpected error: {e}")
		return f'{id} : {return_name}'
		
	def print_contacts(self):
		contacts_list = ''
		for id in self.contact_dict:
			id_adjust = id.ljust(10)
			first = self.contact_dict[id][0].ljust(22)
			last = self.contact_dict[id][1].ljust(22)
			contacts_list += f'{first}{last}{id}\n'
		return contacts_list
