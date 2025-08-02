from sqlalchemy.orm import Session
from models import ParkingSlot, CarSize
from schemas import ParkingSlotCreate
from typing import List, Optional

class ParkingCRUD:
    def create_parking_slot(self, db: Session, slot_data: ParkingSlotCreate) -> ParkingSlot:
        existing_slot = db.query(ParkingSlot).filter(
            ParkingSlot.slot_number == slot_data.slot_number
        ).first()
        
        if existing_slot:
            raise ValueError(f"Parking slot {slot_data.slot_number} is already exist : )")
        
        db_slot = ParkingSlot(**slot_data.model_dump())
        db.add(db_slot)
        db.commit()
        db.refresh(db_slot)
        return db_slot
    
    def get_parking_slot(self, db: Session, slot_id: int) -> Optional[ParkingSlot]:
        return db.query(ParkingSlot).filter(ParkingSlot.id == slot_id).first()
    
    def get_parking_slots(self, db: Session, skip: int = 0, limit: int = 100) -> List[ParkingSlot]:
        return db.query(ParkingSlot).offset(skip).limit(limit).all()
    
    def get_available_slots(self, db: Session) -> List[ParkingSlot]:
        return db.query(ParkingSlot).filter(ParkingSlot.is_occupied == False).all()
    
    def get_available_slots_count(self, db: Session) -> int:
        return db.query(ParkingSlot).filter(ParkingSlot.is_occupied == False).count()
    
    def update_slot_status(self, db: Session, slot_id: int, is_occupied: bool) -> Optional[ParkingSlot]:
        slot = db.query(ParkingSlot).filter(ParkingSlot.id == slot_id).first()
        if slot:
            slot.is_occupied = is_occupied
            db.commit()
            db.refresh(slot)
        return slot

parking_crud = ParkingCRUD()