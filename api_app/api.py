from typing import List, Tuple
from database import engine, SessionLocal
from fastapi import Depends, FastAPI, Query, HTTPException, status
from databases import Database
import schemas
from models import Booking, Client
from sqlalchemy.orm import Session
import crud


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.on_event("startup")
# async def startup():
#     await get_db().connect()


# @app.on_event("shutdown")
# async def shutdown():
#     await get_db().disconnect()


async def pagination(
    offset: int = Query(0, ge=0),
    limit: int = Query(50, ge=0),
) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (offset, capped_limit)


@app.get("/bookings", response_model=list[schemas.BookingBase])
async def list_bookings(
    pagination: Tuple[int, int] = Depends(pagination), db: Session = Depends(get_db)
):
    offset, limit = pagination
    return crud.get_bookings(db, offset, limit)


@app.get("/bookings/{id}", response_model=schemas.BookingBase)
async def single_booking(id: int, db: Session = Depends(get_db)):
    bkg = crud.get_booking(db, id)
    if bkg is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return bkg
