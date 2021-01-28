from models.user import User
from decimal import Decimal
import peewee as pw

class Student(User):
    rating = pw.DecimalField(default=Decimal(5))
