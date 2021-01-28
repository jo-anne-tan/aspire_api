from models.user import User
import peewee as pw

class Tutor(User):
    rating = pw.DecimalField()
