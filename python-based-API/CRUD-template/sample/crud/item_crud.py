from sqlalchemy.orm import Session
from app import models, schemas
from typing import List


def get_items(db: Session, skip: int = 0, limit: int = 10) -> List[models.Item]:
    return db.query(models.Item).filter(models.Item.is_active == True).offset(skip).limit(limit).all()

def get_item(db: Session, item_id: int) -> models.Item:
    return db.query(models.Item).filter(models.Item.id == item_id, models.Item.is_active == True).first()

def create_item(db: Session, item: schemas.ItemCreate) -> models.Item:
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, item: schemas.ItemUpdate) -> models.Item:
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        for key, value in item.dict(exclude_unset=True).items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int) -> bool:
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item:
        db_item.is_active = False
        db.commit()
        return True
    return False
