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
    title = pw.CharField(null=False)
    price = pw.DecimalField(null=False)
    duration = pw.IntegerField(null=False)
    start_time=pw.DateTimeField(null=False)
    end_time=pw.DateTimeField(null=False)
    max_student_capacity=pw.IntegerField(null=False)
    status=pw.CharField(null=False)
    status_timestamp=pw.DateTimeField(default=datetime.datetime.now)

    # WIP : may not require this validation if api for picking meeting time will handle this.
    # To revisit if api cannot handling time conflicts!
    
    # # validation
    # # check for clashing times with same tutor
    # def validation(self):
    #     all_sessions = Tutor_session.select().where(Tutor_session.tutor == self.tutor)

    #     for session in all_sessions:
    #         overlap_1 = (session.start_time<= self.start_time) and (self.start_time < session.end_time)
    #         overlap_2 = session.
    #         # existing session : 3-5pm
    #         # new session      : 4-5pm

    #         # overlap occurs when new session start_time is between existing session's start and end time
    #         if (session.start_time <= self.start_time and self.start_time < session.end_time)or (session.start_time== self.start_time or session.end_time == self.end_time):
    #         # or if two sessions share the same start_time or end_time
                
    #             self.errors.append(f"The session overlaps with session id {session.id} for '{session.title}', {start_time} to {end_time}")
