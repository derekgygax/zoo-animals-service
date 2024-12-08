from sqlalchemy import Column, Enum, String, Date, DateTime, func, UniqueConstraint, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates
from uuid import uuid4
from datetime import datetime
import pytz

# Local
from app.database import Base

class Breeding(Base):
    __tablename__ = "breeding"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, name="id")
    parent_1_id = Column(UUID(as_uuid=True), ForeignKey("animal.id", ondelete="RESTRICT"), nullable=False, name="parent_1_id")
    parent_2_id = Column(UUID(as_uuid=True), ForeignKey("animal.id", ondelete="RESTRICT"), nullable=False, name="parent_2_id")
    offspring_id = Column(UUID(as_uuid=True), ForeignKey("animal.id", ondelete="RESTRICT"), nullable=False, name="offspring_id")
    occurred_at = Column(DateTime(timezone=True), nullable=False, name="occurred_at")

    # Timestamps - keep track of when entry was created and updated. maybe need in future
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), nullable=False, name="created_at")
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(pytz.UTC), onupdate=func.now(), nullable=False, name="updated_at")

    # Relationships back to Animal
    parent_1 = relationship("Animal", foreign_keys=[parent_1_id], back_populates="breeding_parent_1")
    parent_2 = relationship("Animal", foreign_keys=[parent_2_id], back_populates="breeding_parent_2")
    offspring = relationship("Animal", foreign_keys=[offspring_id], back_populates="breeding_offspring")

    @validates('created_at')
    def validate_created_at(self, key, value):
        # Raise an error if `created_at` is attempted to be changed
        if getattr(self, key) is not None:
            raise ValueError("The `created_at` field cannot be modified after creation.")
        return value
    
    # Composite unique constraint
    __table_args__ = (
        UniqueConstraint('parent_1_id', 'parent_2_id', 'offspring_id', name='unique_breeding_combination'),
    )

# TODO FOR RETRIEVING THE TIMEZONE!!
# # Assuming `post.created_at` is a timezone-aware datetime in UTC
# user_timezone = pytz.timezone("America/New_York")  # Example user timezone
# local_time = post.created_at.astimezone(user_timezone)
# print(local_time)  # This will display the time converted to the user's timezone