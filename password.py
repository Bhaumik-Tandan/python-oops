"""
Question 9: Private Methods and Properties
Design a class PasswordManager to manage passwords. 
Implement private methods to generate a strong password and a private attribute to store the passwords securely. 
Provide methods to add, retrieve, and update passwords.
"""

import random
import string

class PasswordManager:
    def __init__(self):
        self.__passwords = {}

    def __generate_password(self):
        chars = string.ascii_letters + string.digits + string.punctuation
        return "".join(random.choice(chars) for _ in range(10))

    def add_password(self, website):
        password = self.__generate_password()
        self.__passwords[website] = password

    def get_password(self, website):
        return self.__passwords.get(website, None)

    def update_password(self, website):
        if website in self.__passwords:
            password = self.__generate_password()
            self.__passwords[website] = password
        else:
            raise ValueError("Website not found")

    
# Creating a password manager
pm = PasswordManager()

# Adding passwords
pm.add_password("google.com")
pm.add_password("facebook.com")
pm.add_password("twitter.com")

print(pm.get_password("google.com"))
print(pm.get_password("facebook.com"))
print(pm.get_password("twitter.com"))

# Updating passwords    
pm.update_password("google.com")
pm.update_password("facebook.com")
pm.update_password("twitter.com")

print(pm.get_password("google.com"))
print(pm.get_password("facebook.com"))
print(pm.get_password("twitter.com"))



