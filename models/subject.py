import peewee as pw
from models.base_model import BaseModel

class Subject(BaseModel):
    category = pw.CharField(null=False)
    description = pw.TextField()

    