from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.core.dependencies import get_current_active_user
from app.crud import item as item_crud
from app.schemas.item import Item, ItemCreate, ItemUpdate

router = APIRouter()

@router.post("/items/", response_model=Item)
def create_item_for_current_user(
    item: ItemCreate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)
):
    return item_crud.create_item(db=db, item=item, owner_id=current_user.id)

@router.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = item_crud.get_items(db, skip=skip, limit=limit)
    return items

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = item_crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/items/{item_id}", response_model=Item)
def update_item(
    item_id: int, item: ItemUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)
):
    db_item = item_crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    if db_item.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return item_crud.update_item(db=db, item_id=item_id, item_update=item)

@router.delete("/items/{item_id}", response_model=Item)
def delete_item(
    item_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)
):
    db_item = item_crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    if db_item.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return item_crud.delete_item(db=db, item_id=item_id)