from typing import Optional

from pydantic import BaseModel, constr, conlist


class AnnouncementBase(BaseModel):
    name: constr(max_length=200)
    price: float

    class Config:
        orm_mode = True


class AnnouncementListView(AnnouncementBase):
    main_photo: str


class AnnouncementCreate(AnnouncementBase):
    description: Optional[constr(max_length=1000)]
    photos: Optional[conlist(str, max_items=3)] = []


class AnnouncementCreateResponse(BaseModel):
    id: int
    success: bool = True

    class Config:
        orm_mode = True
