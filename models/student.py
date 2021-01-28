from models.user import User
import peewee as pw

class Student(User):
    rating = pw.DecimalField()
