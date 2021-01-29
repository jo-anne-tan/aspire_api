import peewee as pw
from models.base_model import BaseModel

class Subject(BaseModel):
    category = pw.CharField(null=False, unique=True)
    description = pw.TextField(default="")

    #validation
    def validate(self):
        if Subject.get_or_none(Subject.category==self.category):
            self.errors.append("This category already exists.")