
from sqlalchemy import Column, Enum, String, Date, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates
from uuid import uuid4
from datetime import datetime
import pytz

# Local
from app.enums.gender import GENDER
from app.enums.health_type import HEALTH_TYPE
from app.enums.specie import SPECIE
from app.database import Base

# Other models
from app.models.event import Event
from app.models.medical_record import MedicalRecord

# NOTE!!:
#   You do NOT need name to define the column name unless the 
#   the column name is different than the attribute
#   This is just there to show how

class Animal(Base):
    __tablename__ = "animal"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, name="id")
    name = Column(String(100), nullable=False, name="name")
    specie = Column(String(100), ForeignKey("specie.specie", ondelete="RESTRICT"), nullable=False, name="specie")
    gender = Column(Enum(GENDER), nullable=False, name="gender")
    health = Column(Enum(HEALTH_TYPE), nullable=False, name="health")
    dob = Column(Date, nullable=False, name="dob")
    acquisition_date = Column(Date, nullable=False, name="acquisition_date")

    # Timestamps - keep track of when entry was created and updated. maybe need in future
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), nullable=False, name="created_at")
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), onupdate=func.now(), nullable=False, name="updated_at")

    # Relations back to specie
    specie_relationship = relationship("Specie", foreign_keys=[specie], back_populates="animals")

	# Relationship to medical_record (One-to-Many)
    medical_records = relationship("MedicalRecord", foreign_keys=[MedicalRecord.animal_id], back_populates="animal", cascade="all, delete-orphan")

    # Relationship to events (One-to-Many)
    events = relationship("Event", foreign_keys=[Event.animal_id], back_populates="animal", cascade="all, delete-orphan")

    @validates('created_at')
    def validate_created_at(self, key, value):
        # Raise an error if `created_at` is attempted to be changed
        if getattr(self, key) is not None:
            raise ValueError("The `created_at` field cannot be modified after creation.")
        return value

# TODO FOR RETRIEVING THE TIMEZONE!!
# # Assuming `post.created_at` is a timezone-aware datetime in UTC
# user_timezone = pytz.timezone("America/New_York")  # Example user timezone
# local_time = post.created_at.astimezone(user_timezone)
# print(local_time)  # This will display the time converted to the user's timezone