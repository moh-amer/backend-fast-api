from pydantic import BaseModel
from typing import Optional, List
from app.schemas.item import Item

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    email: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        from_attributes = True