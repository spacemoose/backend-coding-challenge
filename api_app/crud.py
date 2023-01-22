from sqlalchemy.orm import Session
from fastapi import Query, Depends
from models import Skill

import models, schemas


def get_booking(db: Session, id: int):
    return db.query(models.Booking).filter(models.Booking.id == id).first()

def get_bookings(db: Session, skip: int, limit: int):
    return db.query(models.Booking).offset(skip).limit(limit).all()

def get_required_skills(db: Session, booking_id: int) -> list[Skill]:
    vals =  db.query(models.RequiredSkills).where(models.RequiredSkills.bookingId == booking_id)
    retval = []
    for val in vals:
        retval.append(val.skill)
    return retval

def get_optional_skills(db: Session, booking_id: int) -> list[Skill]:
    vals = db.query(models.OptionalSkills).where(models.OptionalSkills.bookingId == booking_id)
    retval = []
    for val in vals:
        retval.append(val.skill)
    return retval
