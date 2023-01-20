from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Talent(BaseModel):
    talentID: str
    talentName: str
    talentGrade: str

class Client(BaseModel):
    client: str
    clientName: str
    industry: str

class Skill(BaseModel):
    name: str
    category: str

class Booking(BaseModel):
    id: int
    bookingGrade: str
    originalId: str
    operatingUnit: str
    officeCity: str
    officePostalCode: str
    totalHours: str
    startDate: datetime
    endDate: datetime
    isUnassigned: bool
    clientId: str
    talentId: str
    jobManager: Optional[Talent] = None
    clientName: Optional[str]
    industry: Optional[str]
    talent: Optional[Talent] = None
    optionalSkills: Optional[list] = None
    requiredSkills: Optional[list] = None

class BookingCreate(Booking):
    pass
# do i need pydantic models for requiredskills & optionalskills?
