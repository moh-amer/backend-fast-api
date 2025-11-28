from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database.database import get_db
from app.core.dependencies import get_current_active_user
from app.crud import user as user_crud
from app.schemas.user import User, UserUpdate

router = APIRouter()

@router.get("/users/me/", response_model=User)
def read_users_me(current_user = Depends(get_current_active_user)):
    return current_user

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/users/me/", response_model=User)
def update_user_me(user_update: UserUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_active_user)):
    updated_user = user_crud.update_user(db, current_user.id, user_update)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user