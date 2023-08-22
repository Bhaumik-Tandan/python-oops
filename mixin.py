"""
Question 10: Mixins
Create a mixin class LoggerMixin with methods to log messages. 
Implement classes Database and Filesystem that use the LoggerMixin to log various actions like reading, writing, or querying data. 
Show how you can reuse the logging functionality in multiple classes.
"""

class LoggerMixin:
    def log(self, message):
        print(message)

class Database(LoggerMixin):
    def read(self):
        self.log("Reading data from database")

    def write(self):
        self.log("Writing data to database")

    def query(self):
        self.log("Querying data from database")

class Filesystem(LoggerMixin):
    def read(self):
        self.log("Reading data from filesystem")

    def write(self):
        self.log("Writing data to filesystem")

    def query(self):
        self.log("Querying data from filesystem")

db = Database()
db.read()
db.write()
db.query()

fs = Filesystem()
fs.read()
fs.write()
