# This file shall only run once upon initiation
# To be placed in Procfile -> release: section

# if there are no subjects in database yet,
# create a list of preset subjects.

# WIP : running python preset_subjects.py returns KeyError: 'DATABASE_URL'
# Most likely caused by environment variables not loaded
#   File "/home/joannetan/aspire_api/database.py", line 15, in return_db
#     db_config = parse_db_url(os.environ['DATABASE_URL'])
#   File "/home/joannetan/anaconda3/envs/ASPIRE/lib/python3.9/os.py", line 679, in __getitem__
#     raise KeyError(key) from None



from models.subject import Subject

print("Loading environment variables from .env")
from dotenv import load_dotenv
load_dotenv()


exist_subjects = Subject.select()

if not len(exist_subjects):
    presets =["Language", "Mathematics","Coding", "Accounting", "Life Skills"]
    for p in presets:
        subject = Subject(category=p)
        print(subject)
        if subject.save():
            print(f"Subject {p} saved.")
        else:
            print(f"Unable to create subject {p}.")