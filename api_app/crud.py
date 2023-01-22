from sqlalchemy.orm import Session
from fastapi import Query, Depends


import models, schemas


def get_booking(db: Session, id: int):
    return db.query(models.Booking).filter(models.Booking.id == id).first()

#    joined = dict(**booking_data)
#    client_select = Client.select().where(Client.c.clientId == booking_data["clientId"])
#    client_data = await database.fetch_one(client_select)
#    joined.update(**client_data)

def get_bookings(db: Session, skip: int, limit: int):
    return db.query(models.Booking).offset(skip).limit(limit).all()
