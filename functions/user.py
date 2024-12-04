from fastapi import HTTPException, UploadFile, File, Depends
from sqlalchemy.orm import Session

from db import database
from models.user import Users
from routes.login import get_password_hash, get_current_active_user
from schemas.user import CreateUser
from utils.image_save import save_file


def user_image(file: UploadFile = File(...), db: Session = Depends(database),
               current_user: CreateUser = Depends(get_current_active_user)):
    image_filename = save_file(file)
    user = db.query(Users).filter(Users.id == current_user.id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User topilmadi")
    user.image = image_filename
    db.commit()


def create_admin(form, db):
   if form.email.endswith('@gmail.com') or form.email.endswith('@email.com'):
       new_item_db = Users(
            name=form.name,
            username=form.username,
            email=form.email,
            role="admin",
            password=get_password_hash(form.password))
       db.add(new_item_db)
       db.commit()
   else:
       raise HTTPException(400, "Emailni togri kiriting!")




def update_admin(form, db, current_user):
    if current_user.role == "admin":
        db.query(Users).filter(Users.id == current_user.id).update({
            Users.name: form.name,
            Users.username: form.username,
            Users.email: form.email,
            Users.role: "admin",
            Users.password: get_password_hash(form.password)
        })
        db.commit()
    else:
        raise HTTPException(400, "Siz boshqalarni malumotini o'zgartirolmaysiz !")


def delete_user(db, user):
    db.query(Users).filter(Users.id == user.id).delete()
    db.commit()
