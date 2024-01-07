class UserProfile:
    def __init__(self, username, email, password, security_question):
        self.__username = username
        self.__email = email
        self.__password = password
        self.__security_question = security_question

    def get_username(self):
        return self.__username

    def get_email(self):
        return self.__email

    def get_security_question(self):
        return self.__security_question

    def set_password(self, new_password):
        self.__password = new_password

    def set_security_question(self, new_security_question):
        self.__security_question = new_security_question

    def display_user_profile(self):
        print(f"Username: {self.__username}")
        print(f"Email: {self.__email}")
        print(f"Security Question: {self.__security_question}")

user_profile = UserProfile(username="john_doe", email="john.doe@example.com", password="securepassword", security_question="What is your favorite color?")

print("Username:", user_profile.get_username())
print("Email:", user_profile.get_email())
print("Security Question:", user_profile.get_security_question())

user_profile.set_password("new_secure_password")
user_profile.set_security_question("What is your favorite movie?")

user_profile.display_user_profile()