from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, Enum
from sqlalchemy.sql import func
from database import Base
import enum

class CarSize(enum.Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

class ParkingSlot(Base):
    __tablename__ = "parking_slots"
    
    id = Column(Integer, primary_key=True, index=True)
    slot_number = Column(String, unique=True, index=True, nullable=False)
    is_occupied = Column(Boolean, default=False)
    size_category = Column(Enum(CarSize), nullable=False)
    x_location = Column(Float, nullable=False)  
    y_location = Column(Float, nullable=False)  
    floor_level = Column(Integer, default=1)
    zone = Column(String, nullable=False) # A, B, C 
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
