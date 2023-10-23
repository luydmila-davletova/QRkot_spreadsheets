from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field


class DonationBase(BaseModel):
    full_amount: int = Field(gt=0)
    invested_amount: int = 0
    fully_invested: bool = False
    close_date: datetime = None
    comment: Optional[str] = None

    class Config:
        extra = Extra.forbid


class CreateDonationBase(DonationBase):
    pass


class DonationBaseDB(DonationBase):
    id: int
    user_id: int
    create_date: datetime
    invested_amount: Optional[int] = 0
    fully_invested: Optional[bool] = False

    class Config:
        orm_mode = True


class DonationUserDB(BaseModel):
    id: int
    comment: Optional[str]
    full_amount: int
    create_date: datetime

    class Config:
        orm_mode = True
