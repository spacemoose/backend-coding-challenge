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

def get_metadata():
    return metadata

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
