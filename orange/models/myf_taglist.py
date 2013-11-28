# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_taglist_table='myf_taglist'

class Myf_taglist(Base):

    __tablename__ = myf_taglist_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id=Column(Integer,primary_key=True)
    arctype_id=Column(Integer,nullable=False, server_default='0')
    name=Column(String(50),nullable=False)
    img_path=Column(String(100),nullable=False)
    create_date=Column(DATETIME,nullable=False)
    update_date=Column(DATETIME,nullable=False)
    create_by=Column(String(50),nullable=False)
    update_by=Column(String(50),nullable=False)
    del_flag=Column(Integer,nullable=False, server_default='0')
    tag_type=Column(Integer,nullable=True)
    typeid=Column(Integer,nullable=False, server_default='0')