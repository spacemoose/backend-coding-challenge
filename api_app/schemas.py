from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from typing import Any

class TalentBase(BaseModel):
    talentId: Optional[str] = None
    talentName: Optional[str] = None
    talentGrade: Optional[str] = None

    class Config:
        orm_mode=True

class ClientBase(BaseModel):
    clientId: str
    clientName: Optional[str] = None
    industry: Optional[str] = None

    class Config:
        orm_mode=True

class SkillBase(BaseModel):
    name: str
    category: str

    class Config:
        orm_model=True

class BookingBase(BaseModel):
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
    clientId: Optional[str] = None
    talentId: Optional[str] = None
    jobManagerId: Optional[str] = None
    client: ClientBase
    talent:     Optional[TalentBase] = None
    jobManager: Optional[TalentBase] = None
    optionalSkills: Optional[list[Any]] = None
    requiredSkills: Optional[list[Any]] = None

    class Config:
        orm_mode=True
