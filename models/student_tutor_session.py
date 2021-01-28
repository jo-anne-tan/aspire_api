import datetime
import peewee as pw
from models.tutor import Tutor
from models.subject import Subject
from models.base_model import BaseModel
from models.student import Student
from models.tutor_session import Tutor_session

class Student_tutor_session(BaseModel):
    student = pw.ForeignKeyField(Student, backref="student_tutor_sessions")
    tutor_session = pw.ForeignKeyField(Tutor_session, backref="student_tutor_sessions")
    status = pw.CharField(null=True)
    status_timestamp = pw.DateTimeField(default=datetime.datetime.now)
    zoom_url = pw.CharField()