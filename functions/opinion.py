from fastapi import HTTPException, UploadFile, Depends, File
from sqlalchemy.orm import Session

from db import database
from models.opinion import Opinion
from routes.login import get_current_active_user
from schemas.opinion import CreateOpinion
from utils.image_save import save_file


def create_opinion(form, db, current_user):
    if current_user.role == "admin":
        new_opinion = Opinion(
            full_name=form.full_name,
            text=form.text
        )
        db.add(new_opinion)
        db.commit()

def update_opinion(ident, form, db, current_user):
    if current_user.role == "admin":
        course = db.query(Opinion).filter(Opinion.id == ident).first()
        if not course:
            raise HTTPException(status_code=404, detail="Opinion topilmadi")
        db.query(Opinion).filter(Opinion.id == ident).update({
            Opinion.full_name: form.full_name,
            Opinion.text: form.text
        })
        db.commit()
        db.refresh(course)


def opinion_video(ident, file: UploadFile = File(...), db: Session = Depends(database),
                 current_user: CreateOpinion = Depends(get_current_active_user)):
    if current_user.role == "admin":
        video_filename = save_file(file)
        course = db.query(Opinion).filter(Opinion.id == ident).first()
        if not course:
            raise HTTPException(status_code=404, detail="Course topilmadi")
        course.video = video_filename
        db.commit()


def delete_opinion(openion_id, db, current_user):
    if current_user.role == "admin":
        opinion = db.query(Opinion).filter(Opinion.id == openion_id).first()
        if not opinion:
            raise HTTPException(status_code=404, detail="Opinion not found")
        db.delete(opinion)
        db.commit()
    else:
        raise HTTPException(400, "Error")