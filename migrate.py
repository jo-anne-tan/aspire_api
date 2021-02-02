import os

os.environ['MIGRATION'] = '1'

if not os.getenv('FLASK_ENV') == 'production':
    print("Loading environment variables from .env")
    from dotenv import load_dotenv
    load_dotenv()

import peeweedbevolve
from models import *
from models.base_model import db
# Production
print("Running Migration")
if os.getenv('FLASK_ENV') == 'production':
    db.evolve(ignore_tables={'base_model'}, interactive=False)
else:
    db.evolve(ignore_tables={'base_model'})
print("Finish Migration")


from models.subject import Subject
exist_subjects = Subject.select()
print("Setting Preset Subjects")
if not len(exist_subjects):
    presets =["Language", "Mathematics","Coding", "Accounting", "Life Skills"]
    for p in presets:
        subject = Subject(category=p)
        print(subject)
        if subject.save():
            print(f"Subject {p} saved.")
        else:
            print(f"Unable to create subject {p}.")
print("Finish Setting Up Preset Subjects")
