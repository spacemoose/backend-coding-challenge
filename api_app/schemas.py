from pydantic import BaseModel
from datetime import datetime
from typing import Optional

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

class ClientCreate(ClientBase):
    pass

class SkillBase(BaseModel):
    name: str
    category: str

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
 #   talentId: Optional[str] = None
    jobManagerId: Optional[str] = None
    client: ClientBase
    jobManager: Optional[TalentBase] = None
#    talent: Optional[TalentBase] = None
    # optionalSkills: Optional[list[SkillBase]] = None
    # requiredSkills: Optional[list] = None

    class Config:
        orm_mode=True

class BookingCreate(BookingBase):
    pass
# do i need pydantic models for requiredskills & optionalskills?
