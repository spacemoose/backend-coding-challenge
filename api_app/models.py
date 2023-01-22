from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Numeric,
    DateTime,
    Table,
)
from sqlalchemy.orm import relationship, declarative_base, backref

Base = declarative_base()


class Talent(Base):
    __tablename__ = "talent"

    talentId = Column(String, primary_key=True, index=True)
    talentName = Column(String)
    talentGrade = Column(String)

    def __repr__(self):
        return f"Talent(talentId={self.talentId!r}, talentName={self.talentNname!r}, talentGrade={self.talentGrade!r})".format(
            self=self
        )


class Client(Base):
    __tablename__ = "client"

    clientId = Column(String, primary_key=True)
    clientName = Column(String)
    industry = Column(String)

    def __repr__(self):
        return f"Client(clientId={self.clientId}, clientName={self.clientName}, industry={self.industry})".format(
            self=self
        )


class Booking(Base):
    __tablename__ = "booking"

    id = Column(Integer, primary_key=True)
    originalId = Column(String, nullable=False)
    bookingGrade = Column(String)
    operatingUnit = Column(String, nullable=False)
    officeCity = Column(String)
    officePostalCode = Column(String)
    totalHours = Column(Numeric, nullable=False)
    startDate = Column(DateTime, nullable=False)
    endDate = Column(DateTime, nullable=False)
    isUnassigned = Column(Boolean, nullable=False)
    clientId = Column(String(), ForeignKey("client.clientId"))
    talentId = Column(String(), ForeignKey("talent.talentId"))
    jobManagerId = Column(String(), ForeignKey("talent.talentId"))
    client = relationship("Client")

    jobManager = relationship("Talent", foreign_keys=[jobManagerId])
    talent =     relationship("Talent", foreign_keys=[talentId])


    def __repr__(self):
        return f"""Bookings(id={self.id}, originalId={self.originalId}, bookingGrade={self.bookingGrade},
        operatingUnit={self.operatingUnit}, officeCity={self.officeCity}, officePostalCode = {self.officePostalCode},
        totalHours={self.totalHours}, startDate={self.startDate}, endDate={self.endDate}, isUnassigned={self.isUnassigned},
        clientId={self.clientId}, talentId={self.talentId}, jobManagerId={self.jobManagerId})""".format(
            self=self
        )


class RequiredSkill(Base):
    __tablename__ = "requiredSkills"
    id = Column(Integer, primary_key=True)
    bookingId = Column(Integer, ForeignKey("booking.id"))
    skillName = Column(String, ForeignKey("skill.name"))

    def __repr__(self):
        return f"bookingId={self.bookingId}, skillName={self.bookingId}, skill={self.skill}.format(self=self)"


class OptionalSkill(Base):
    __tablename__ = "optionalSkills"
    id = Column(Integer, primary_key=True)
    bookingId = Column(Integer, ForeignKey("booking.id"))
    skillName = Column(String, ForeignKey("skill.name"))
    skill = relationship("Skill")


class Skill(Base):
    __tablename__ = "skill"

    name = Column(String, primary_key=True)
    category = Column(String)

    #   requiredSkills = relationship(Booking, secondary=RequiredSkill, back_populates="requiredSkills")
    #   optionalSkills = relationship(Booking, secondary=OptionalSkill, back_populates="optionalSkills")

    def __repr__(self):
        return f"Skill(name={self.name}, category = {self.category})".format(self=self)
