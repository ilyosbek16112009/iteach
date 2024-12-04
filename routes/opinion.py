from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from db import database
from functions.opinion import create_opinion, update_opinion, delete_opinion, opinion_video
from models.opinion import Opinion
from routes.login import get_current_active_user
from schemas.opinion import CreateOpinion
from schemas.user import CreateUser

opinion_router = APIRouter(
    prefix="/opinions",
    tags=["Opinions"]
)

@opinion_router.get("/get_opinion")
def get(db: Session = Depends(database)):
    return db.query(Opinion).all()


@opinion_router.post("/create_opinion")
def create_new_opinion(form: CreateOpinion, db: Session = Depends(database),
                       current_user: CreateUser = Depends(get_current_active_user)):
    create_opinion(form, db, current_user)
    raise HTTPException(200, "Amaliyiot muvafaqiyatli amalga oshirildi")

@opinion_router.post('/upload-video')
def video_yuklas(ident: int = 0, file: UploadFile = File(...), db: Session = Depends(database),
                 current_user: CreateUser = Depends(get_current_active_user)):
    opinion_video(ident, file, db, current_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvafaqiyatli amalga oshirildi!")

@opinion_router.put("/update_opinion")
def update_existing_opinion(ident: int, form: CreateOpinion,  db: Session = Depends(database),
                            current_user: CreateUser = Depends(get_current_active_user),):
    update_opinion(ident, form, db, current_user)
    raise HTTPException(200, "Amaliyot muvafaqiyatli amalga oshirildi")

@opinion_router.delete("/delete_opinion")
def delete_existing_opinion(opinion_id: int, db: Session = Depends(database),
                            current_user: CreateUser = Depends(get_current_active_user)):
     delete_opinion(opinion_id, db, current_user)
     raise HTTPException(200, "Amaliyot muvafaqiyatli amalga oshirildi")
