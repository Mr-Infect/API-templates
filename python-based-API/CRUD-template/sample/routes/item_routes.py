from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database
from typing import List

router = APIRouter(prefix="/items", tags=["Items"])

@router.get("/", response_model=List[schemas.ItemOut])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.item_crud.get_items(db, skip, limit)

@router.get("/{item_id}", response_model=schemas.ItemOut)
def read_item(item_id: int, db: Session = Depends(database.get_db)):
    item = crud.item_crud.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/", response_model=schemas.ItemOut)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    return crud.item_crud.create_item(db, item)

@router.patch("/{item_id}", response_model=schemas.ItemOut)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(database.get_db)):
    updated = crud.item_crud.update_item(db, item_id, item)
    if updated is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    if not crud.item_crud.delete_item(db, item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"deleted": True}
