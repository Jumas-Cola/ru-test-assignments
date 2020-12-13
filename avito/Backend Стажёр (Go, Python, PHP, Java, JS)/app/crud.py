from sqlalchemy.orm import Session
import json
from urllib.request import urlopen
from operator import neg
from fastapi import HTTPException

from . import models, schemas
from .sqlalchemy_pagination import paginate


def get_announcement(db: Session, announcement_id: int):
    return db.query(models.Announcement).filter(models.Announcement.id == announcement_id).first()


def get_announcements(db: Session, page: int = 1, order: str = 'id', reverse: bool = False):
    order = getattr(models.Announcement, order)
    i = paginate(db.query(models.Announcement).order_by(
        neg(order) if reverse else order), page, page_size=10).items
    for r in i:
        r.main_photo = json.loads(r.photos)[0]
    return i


def create_announcement(db: Session, announcement: schemas.AnnouncementCreate):
    db_announcement = models.Announcement(
        name=announcement.name,
        price=announcement.price,
        description=announcement.description,
        photos=json.dumps(announcement.photos)
    )
    for url in announcement.photos:
        if not check_img_url_valid(url):
            raise HTTPException(status_code=404, detail='Image url incorrect')
    db.add(db_announcement)
    db.commit()
    db.refresh(db_announcement)
    return db_announcement


def check_img_url_valid(url: str) -> bool:
    image_formats = ('image/png', 'image/jpeg', 'image/gif')
    try:
        r = urlopen(url)
    except:
        return False
    if r.code not in (200, 209):
        return False
    meta = r.info()
    if 'content-type' in meta and meta['content-type'] in image_formats:
        return True
    return False


def filter_announcement_fields(q, fields) -> dict:
    q.photos = json.loads(q.photos)
    q.main_photo = q.photos[0]
    response = q.__dict__
    items_to_remove = {'created_at', 'id',
                       'photos', 'description'} - set(fields)
    for k in items_to_remove:
        response.pop(k, None)
    return response
