
from sqlalchemy import Column, String, DateTime, func
from sqlalchemy.orm import relationship, validates
from datetime import datetime
import pytz

# Local
from app.database import Base

# Other models
from app.models.animal import Animal

class Specie(Base):
    __tablename__ = "specie"

    id = Column(String(100), primary_key=True, nullable=False, name="id")
    description = Column(String(500), nullable=False, name="description")

    # Timestamps - keep track of when entry was created and updated. maybe need in future
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), nullable=False, name="created_at")
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), onupdate=func.now(), nullable=False, name="updated_at")

    # Relationship to animals (One-to-Many)
    animals = relationship("Animal", back_populates="specie", cascade="save-update")

    @validates('id')
    def validate_specie(self, key, value):
        # Force lowercase before insertion
        return value.lower()

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