import email
from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(BaseModel):
    password: str

class User(BaseModel):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True