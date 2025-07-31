from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from models import CarSize

class ParkingSlotCreate(BaseModel):
    slot_number: str = Field(..., description="")
    size_category: CarSize = Field(..., description="")
    x_location: float = Field(..., description="X location")
    y_location: float = Field(..., description="Y location")
    floor_level: int = Field(default=1, description="Floor level")
    zone: str = Field(..., description="Zone N.")

class ParkingSlotResponse(BaseModel):
    id: int
    slot_number: str
    is_occupied: bool
    size_category: CarSize
    x_location: float
    y_location: float
    floor_level: int
    zone: str
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True