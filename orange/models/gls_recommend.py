# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

gls_recommend_table = 'gls_recommend'


class Gls_recommend(Base):
    __tablename__ = gls_recommend_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    archive_id = Column(Integer, nullable=True)
    arctype_id = Column(Integer, nullable=True)
    title = Column(String(50), nullable=True)
    url = Column(String(150), nullable=True)
    post_time = Column(DATETIME, nullable=True)
    state = Column(Boolean, nullable=True)
