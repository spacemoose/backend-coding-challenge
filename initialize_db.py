# create the database and populate the tables.
# valuing dev time efficiency over computational efficiency here.

import json
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    MetaData,
    Numeric,
    String,
    Table,
    Identity,
    create_engine,
)
from datetime import datetime

metadata = MetaData()

Talents = Table(
    "talents",
    metadata,
    Column("talentId", String(), primary_key=True),
    Column("talentName", String(), nullable=False),
    Column("talentGrade", String(), nullable=False),
)


Clients = Table(
    "clients",
    metadata,
    Column("clientId", String(), primary_key=True),
    Column("clientName", String),
    Column("industry", String),
)

Skills = Table(
    "skills",
    metadata,
    Column("name", String(),  primary_key=True),
    Column("category", String()),
)

Bookings = Table(
    "bookings",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("originalId", String(), nullable=False, unique=True),
    Column("bookingGrade", String()),
    Column("operatingUnit", String()),
    Column("officeCity", String()),
    Column("officePostalCode", String, nullable=False),
    Column("totalHours", Numeric, nullable=False),
    Column("startDate", DateTime, nullable=False),
    Column("endDate", DateTime, nullable=False),
    Column("isUnassigned", Boolean),
    Column("clientId", String(), ForeignKey("clients.clientId")),
    Column("talentId", String(), ForeignKey("talents.talentId")),
    Column("jobManagerId", String(), ForeignKey("talents.talentId")),
)

RequiredSkills = Table(
    "requiredSkills",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("skillName",  String(), ForeignKey("skills.name")),
    Column("bookingId", Integer, ForeignKey("bookings.id")),
)


OptionalSkills = Table(
    "optionalSkills",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("skillName", String(), ForeignKey("skills.name")),
    Column("bookingId", Integer, ForeignKey("bookings.id")),
)

engine = create_engine("sqlite:///bookings.db")
metadata.create_all(engine)


def get_talents(data):
    # get the non-null talent entries
    consumed = set()
    retval = []
    for val in data:
        if val["talentId"] != "":
            if val["talentId"] not in consumed:
                consumed.add(val["talentId"])
                retval.append(
                    dict((k, val[k]) for k in ("talentId", "talentName", "talentGrade"))
                )
    return retval


def get_clients(data):
    # get the non-null client entries
    consumed = set()
    retval = []
    for val in data:
        if (val["clientId"] != "") and (val["clientId"] not in consumed):
            consumed.add(val["clientId"])
            retval.append(
                dict((k, val[k]) for k in ("clientId", "clientName", "industry"))
            )
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

ins = Talents.insert()
result = connection.execute(ins, get_talents(data))

ins = Clients.insert()
result = connection.execute(ins, get_clients(data))

ins = Skills.insert()
result = connection.execute(ins, get_skills(data))

ins = Bookings.insert()
result = connection.execute(ins, get_bookings(data))

ins = RequiredSkills.insert()
result = connection.execute(ins, get_skills_join("requiredSkills", data))

ins = OptionalSkills.insert()
result = connection.execute(ins, get_skills_join("optionalSkills", data))
