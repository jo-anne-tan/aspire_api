from models.user import User
from decimal import Decimal
import peewee as pw

class Tutor(User):
    rating = pw.DecimalField(default=Decimal(5))
