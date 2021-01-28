import datetime
import peewee as pw
from models.tutor import Tutor
from models.subject import Subject
from models.base_model import BaseModel

class Tutor_session(BaseModel):
    # Note: Can remove either duration or end time
    # Status = confirmed, cancelled, ended (optional: postponed)
    subject = pw.ForeignKeyField(Subject, backref="tutor_sessions")
    tutor = pw.ForeignKeyField(Tutor, backref="tutor_sessions")
    title = pw.CharField(null=True)
    price = pw.DecimalField(null=True)
    duration = pw.IntegerField(null=True)
    start_time=pw.DateTimeField(null=True)
    end_time=pw.DateTimeField(null=True) 
    max_student_capacity=pw.IntegerField(null=True)
    status=pw.CharField(null=True) 
    status_timestamp=pw.DateTimeField(default=datetime.datetime.now)