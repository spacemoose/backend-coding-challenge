from typing import List, Tuple
from database import get_database, engine
from fastapi import Depends, FastAPI, HTTPException, Query, status
from databases import Database
from schemas import Booking
from models import Bookings, Clients

app = FastAPI()


@app.on_event("startup")
async def startup():
    await get_database().connect()


@app.on_event("shutdown")
async def shutdown():
    await get_database().disconnect()


async def pagination(
    offset: int = Query(0, ge=0),
    limit: int = Query(50, ge=0),
) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (offset, capped_limit)


async def get_booking_or_404(
    id: int, database: Database = Depends(get_database)
) -> Booking:
    select_query = Bookings.select().where(Bookings.c.id == id)
    booking_data = await database.fetch_one(select_query)
    if booking_data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    joined = dict(**booking_data)
    client_select = Clients.select().where(Clients.c.clientId == booking_data["clientId"])
    client_data = await database.fetch_one(client_select)
    joined.update(**client_data)
    return Booking(**joined)




@app.get("/bookings")
async def list_bookings(
    pagination: Tuple[int, int] = Depends(pagination),
    database: Database = Depends(get_database),
) -> List[Booking]:
    offset, limit = pagination
    select_query = Bookings.select().offset(offset).limit(limit)
    rows = await database.fetch_all(select_query)
    results = [Booking(**row) for row in rows]
    return results


@app.get("/bookings/{id}", response_model=Booking)
async def get_booking(bkg: Booking = Depends(get_booking_or_404)) -> Booking:
    return bkg
