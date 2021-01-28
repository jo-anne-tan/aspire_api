import re
import peewee as pw
from flask_login import UserMixin
from models.base_model import BaseModel
from werkzeug.security import generate_password_hash

class User(BaseModel,UserMixin):
    first_name = pw.CharField(null=False)
    last_name = pw.CharField(null=False)
    age = pw.IntegerField(null=False)
    is_female = pw.BooleanField(null=False) # True for female, False for male
    email=pw.CharField(null=False, unique=True)
    password=pw.CharField(null=False)
    profile_image=pw.CharField(default="")

    # validations
    def validate(self):
        self.duplicate_check()

        if self.password:
            if not (self.password[0:19] == "pbkdf2:sha256:50000"): # if password is not changed
                self.password_check()


    def password_check(self):
        error_flag = False

        special_char = re.search('[\W]', self.password)
        lowercase = re.search('[a-z]',self.password)
        uppercase = re.search('[A-Z]',self.password)
        number = re.search('[0-9]',self.password)

        if len(self.password) <6:
            self.errors.append("Password must be longer than 6 characters")
            error_flag = True

        if not(special_char and lowercase and uppercase and number):
            self.errors.append("Password must have an uppercase letter, lowercase letter and at least one special character")
            error_flag = True

        if (self.password[0:19] == "pbkdf2:sha256:50000"): # hashed password
            pass
        else:
            self.password = generate_password_hash(self.password)
