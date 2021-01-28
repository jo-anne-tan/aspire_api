from models.user import User
from decimal import Decimal
import peewee as pw

class Tutor(User):
    rating = pw.DecimalField(default=5)

    # validation
    def duplicate_check(self):
        duplicate_email =  Tutor.get_or_none(Tutor.email==self.email)

        if duplicate_email:
            if not duplicate_email.id==self.id: #if the id is not your own
                self.errors.append("Email is already taken. Please try again.")
