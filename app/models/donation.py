from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.base import InvestBase


class Donation(InvestBase):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
