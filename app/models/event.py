from sqlalchemy import Column, Enum, String, Date, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates
from uuid import uuid4
from datetime import datetime
import pytz

# Local
from app.enums.event_type import EVENT_TYPE
from app.database import Base

class Event(Base):
    __tablename__ = "event"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, name="id")
    animal_id = Column(UUID(as_uuid=True), ForeignKey("animal.id", ondelete="CASCADE"), nullable=False, name="animal_id")
    type = Column(Enum(EVENT_TYPE), nullable=False, name="type")
    description = Column(String(1000), nullable=True, name="description")
    occurred_at = Column(DateTime(timezone=True), nullable=False)

    # Timestamps - keep track of when entry was created and updated. maybe need in future
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), nullable=False, name="created_at")
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), onupdate=func.now(), nullable=False, name="updated_at")

    # Relationship back to animal
    animal = relationship("Animal", foreign_keys=[animal_id], back_populates="events")

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