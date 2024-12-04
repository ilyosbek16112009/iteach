from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
from functions.user import delete_user, update_admin, user_image, create_admin
from models.user import Users
from routes.login import get_current_active_user
from schemas.user import CreateUser, UpdateUser
from db import database

users_router = APIRouter(
    prefix="/users",
    tags=["Users operation"]
)


@users_router.get('/get')
def get(db: Session = Depends(database)):
    return db.query(Users).all()


@users_router.post('/create_admin')
def admin_yaratish(form: CreateUser, db: Session = Depends(database)):
    create_admin(form, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@users_router.post('/upload-image')
def rasm_yuklash(file: UploadFile = File(...), db: Session = Depends(database),
                 current_user: CreateUser = Depends(get_current_active_user)):
    user_image(file, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvafaqiyatli amalga oshirildi!")


@users_router.put("/update_admin")
def admin_tahrirlash(form: UpdateUser, db: Session = Depends(database),
                     current_user: CreateUser = Depends(get_current_active_user)):
    update_admin(form, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@users_router.delete("/delete")
def delete_users(db: Session = Depends(database),
                 current_user: CreateUser = Depends(get_current_active_user)):
    delete_user(db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
