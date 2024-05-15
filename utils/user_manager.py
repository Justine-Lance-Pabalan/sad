from .user import User

User_instance = User()

class UserManager:
	Users = []

	def load_users():
		pass

	def save_users():
		pass

	def validate_username(self, username):
		if len(username) <4:
			print("Username must be at least 4 characters long.\n")
			return False

	def validate_password(self, password):
		if len(password) <8:
			print("Password must be at least 8 characters long.\n")
			return False

	def register(self):
		print('\n'*10)
		username = input(str("Enter username (at least 4 characters), or leave blank to cancel: "))
		if username == "":
			print('\n'*10)
			return
		elif self.validate_username(username):
			return
		else:
			password = input(str("Enter password (at least 8 characters), or leave blank to cancel: "))
		if password == "":
			print('\n'*10)
			return
		elif self.validate_password(password):
			return
		elif username in self.Users:
			print("Username already exists.\n")
		else:
			self.Users.append[{username: username, password: password}] 
			print("Registration succesful.")
			return
		
	def login():
		pass