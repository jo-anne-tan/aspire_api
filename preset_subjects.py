# This file shall only run once upon initiation
# To be placed in Procfile -> release: section

# if there are no subjects in database yet,
# create a list of preset subjects.

print("Loading environment variables from .env")
from dotenv import load_dotenv
load_dotenv()

from models.subject import Subject

exist_subjects = Subject.select()

if not len(exist_subjects):
    presets =["Language", "Mathematics","Coding", "Accounting", "Life Skills"]
    for p in presets:
        subject = Subject(category=p)
        if subject.save():
            print(f"Subject {p} saved.")
        else:
            print(f"Unable to create subject {p}.")