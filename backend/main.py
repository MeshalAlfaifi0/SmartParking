from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import uvicorn
from database import SessionLocal, engine
from models import Base, ParkingSlot
from schemas import ParkingSlotCreate, ParkingSlotResponse
from crud import parking_crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Mew"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/parking-slots/", response_model=ParkingSlotResponse, status_code=status.HTTP_201_CREATED)
async def create_parking_slot(
    slot_data: ParkingSlotCreate,
    db: Session = Depends(get_db)
):
    try:
        slot = parking_crud.create_parking_slot(db=db, slot_data=slot_data)
        return slot
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/parking-slots/", response_model=List[ParkingSlotResponse])
async def get_all_parking_slots(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    slots = parking_crud.get_parking_slots(db=db, skip=skip, limit=limit)
    return slots

@app.get("/parking-slots/{slot_id}", response_model=ParkingSlotResponse)
async def get_parking_slot(slot_id: int, db: Session = Depends(get_db)):
    slot = parking_crud.get_parking_slot(db=db, slot_id=slot_id)
    if not slot:
        raise HTTPException(status_code=404, detail="Not found")
    return slot

@app.put("/parking-slots/{slot_id}/occupy")
async def occupy_parking_slot(slot_id: int, db: Session = Depends(get_db)):
    slot = parking_crud.update_slot_status(db=db, slot_id=slot_id, is_occupied=True)
    if not slot:
        raise HTTPException(status_code=404, detail="Not found")
    return {"message": f"Parking slot {slot_id} is occupied"}

@app.put("/parking-slots/{slot_id}/free")
async def free_parking_slot(slot_id: int, db: Session = Depends(get_db)):
    slot = parking_crud.update_slot_status(db=db, slot_id=slot_id, is_occupied=False)
    if not slot:
        raise HTTPException(status_code=404, detail="Not found")
    return {"message": f"Parking slot {slot_id} is free"}


@app.get("/parking-slots/available/count")
async def get_available_slots_count(db: Session = Depends(get_db)):
    count = parking_crud.get_available_slots_count(db=db)
    return {"available_slots": count}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)