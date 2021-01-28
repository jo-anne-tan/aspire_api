import datetime
import peewee as pw
from models.base_model import BaseModel
from models.student_tutor_session import Student_tutor_session

class Payment(BaseModel):
    # status = Pending, Complete, Error
    student_tutor_session = pw.ForeignKeyField(Student_tutor_session, backref="student_tutor_sessions")
<<<<<<< HEAD
    amount = pw.DecimalField(null=True)
    status = pw.CharField(null=True)
=======
    amount = pw.DecimalField(null=False)
    status = pw.CharField(null=False) 
>>>>>>> master
    status_timestamp = pw.DateTimeField(default=datetime.datetime.now)