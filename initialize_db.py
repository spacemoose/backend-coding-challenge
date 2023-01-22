# create the database and populate the tables.
# valuing dev time efficiency over computational efficiency here.

import json
from api_app.models import Base, Talent, Client, Booking, Skill
from api_app.models import RequiredSkill, OptionalSkill
from datetime import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///bookings.db")
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


def get_talents(data):
    # get the non-null talent entries
    consumed = set()
    retval = []
    for val in data:
        if val["talentId"] != "":
            if val["talentId"] not in consumed:
                consumed.add(val["talentId"])
                entries = dict((k, val[k]) for k in ("talentId", "talentName", "talentGrade"))
                retval.append(entries)
    return retval


def get_clients(data):
    # get the non-null client entries
    consumed = set()
    retval = []
    for val in data:
        if (val["clientId"] != "") and (val["clientId"] not in consumed):
            consumed.add(val["clientId"])
            entries = dict((k, val[k]) for k in ("clientId", "clientName", "industry"))
            retval.append(entries)
    return retval


def get_skills(data):
    # get non-null entries for the skills table.
    skills = dict()
    # make a dictionary of skills to categories.
    for val in data:
        for rs in val["requiredSkills"]:
            skills[rs["name"]] = rs["category"]
        for os in val["optionalSkills"]:
            skills[os["name"]] = os["category"]
    # now I have a unique list of skills and categories, put them into the correct field names.

    retval = []
    for key, val in skills.items():
        retval.append({"name": key, "category": val})
    return retval


def get_bookings(data):
    # just the fields that go into bookings.
    fields = [
        "id",
        "originalId",
        "bookingGrade",
        "operatingUnit",
        "officeCity",
        "officePostalCode",
        "totalHours",
        "isUnassigned",
        "clientId",
        "talentId",
        "jobManagerId",
    ]
    retval = []
    for val in data:
        temp = dict((k, val[k]) for k in fields)
        temp["startDate"] = datetime.strptime(val["startDate"], '%m/%d/%Y %H:%M %p')
        temp["endDate"] = datetime.strptime(val["endDate"], '%m/%d/%Y %H:%M %p')
        retval.append(temp)
    return retval

def get_skills_join(fieldname, data):
    #get the table entries for the join tables, table specified by the fieldname ("requiredSkills" or "optionalSkills).
    retval = []
    for val in data:
        for skill in val[fieldname]:
            retval.append({"skillName": skill["name"], "bookingId": val["id"]})
    return retval


infile = open("planning.json")
data = json.load(infile)
connection = engine.connect()

bookings = []
for b in get_bookings(data):
    bookings.append(Booking(**b))
session.bulk_save_objects(bookings)

talents = []
for t in get_talents(data):
    talents.append(Talent(**t))
session.bulk_save_objects(talents)

clients = []
for c in get_clients(data):
    clients.append(Client(**c))
session.bulk_save_objects(clients)

skills = []
for s in get_skills(data):
    skills.append(Skill(**s))
session.bulk_save_objects(skills)

requiredSkills = []
for rs in get_skills_join("requiredSkills", data):
    requiredSkills.append(RequiredSkill(**rs))
session.bulk_save_objects(requiredSkills)

optionalSkills = [ ]
for os in get_skills_join("optionalSkills", data):
    optionalSkills.append(OptionalSkill(**os))
session.bulk_save_objects(optionalSkills)


session.commit()
