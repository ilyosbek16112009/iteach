from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import database
from functions.registered import create_register, update, delete
from models.registered import Register
from routes.login import get_current_active_user
from schemas.registered import CreateRegister
from schemas.user import CreateUser

register_router = APIRouter(
    prefix="/registered",
    tags=["Register"]
)

@register_router.get("/get_register")
def get(db: Session = Depends(database)):
    return db.query(Register).all()


@register_router.post("/create_opinion")
def create_new_opinion(form: CreateRegister, db: Session = Depends(database),
                       current_user: CreateUser = Depends(get_current_active_user)):
    create_register(form, db, current_user)
    raise HTTPException(200, "Amaliyiot muvafaqiyatli amalga oshirildi")


@register_router.put("/update_register")
def update_register(form: CreateRegister, register_id: int, db: Session = Depends(database),
                    current_user: CreateUser = Depends(get_current_active_user)):
     update(form, register_id, db, current_user)
     raise HTTPException(200, "Amaliyiot muvafaqiyatli amalga oshirildi")


@register_router.delete("/delete_register")
def delete_register(register_id: int, db: Session = Depends(database),
                    current_user: CreateUser = Depends(get_current_active_user)):
     delete(db, register_id, current_user)
     raise HTTPException(200, "Amaliyiot muvafaqiyatli amalga oshirildi")
