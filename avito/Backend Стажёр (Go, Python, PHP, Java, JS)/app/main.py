from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/announcements/', response_model=schemas.AnnouncementCreateResponse)
def create_announcement(announcement: schemas.AnnouncementCreate, db: Session = Depends(get_db)):
    return crud.create_announcement(db=db, announcement=announcement)


@app.get('/announcements/', response_model=List[schemas.AnnouncementListView])
def read_announcements(page: int = 1, order: str = 'id', reverse: bool = False, db: Session = Depends(get_db)):
    return crud.get_announcements(db, page=page, order=order, reverse=reverse)


@app.get('/announcements/{announcement_id}')
def read_announcement(announcement_id: int, item_fields: str = '', db: Session = Depends(get_db)):
    db_announcement = crud.get_announcement(
        db, announcement_id=announcement_id)
    if db_announcement is None:
        raise HTTPException(status_code=404, detail='Announcement not found')
    response = crud.filter_announcement_fields(
        db_announcement, (i.strip() for i in item_fields.split(',')))
    return response
