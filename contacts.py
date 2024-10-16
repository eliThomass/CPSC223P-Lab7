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
		except:
			print("Unexpected error.")
	def add_contact(self, id, first_name, last_name):
		if id in self.contact_dict.keys():
			return "error"
		fullname = [first_name, last_name]
		self.contact_dict[id] = fullname
		self.contact_dict = dict(sorted(self.contact_dict.items(), key=lambda item: item[1]))
		try:
			with open(self.name, 'w') as f:
				json.dump(self.contact_dict,f)
		except Exception as e:
			print(f"Unexpected error: {e}")
		return self.contact_dict[id]
		
	
