# coding: utf-8

from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey, text
from .database import Base

myf_user_table = 'myf_user'


class Myf_user(Base):
    __tablename__ = myf_user_table

    #__table_args__ = {
    #    'mysql_engine': 'InnoDB',
    #    'mysql_charset': 'utf8'
    #}

    id = Column(Integer, primary_key=True)
    nanme = Column(String(30), nullable=True)
    password = Column(String(30), nullable=True)
    dlm = Column(String(20), nullable=True)
    mail = Column(String(30), nullable=True)
    qq = Column(String(20), nullable=True)
    telephone = Column(String(20), nullable=True)
    microblog = Column(String(20), nullable=True)
    renren = Column(String(20), nullable=True)
    watercress = Column(String(20), nullable=True)
    img = Column(String(80), nullable=True)
    nickname = Column(String(30), nullable=True)
    birthday = Column(DATETIME, nullable=True)
    constellation = Column(String(30), nullable=True)
    school = Column(String(30), nullable=True)
    grade = Column(String(30), nullable=True)
    address = Column(String(30), nullable=True)
    post = Column(String(30), nullable=True)
    real_name = Column(String(30), nullable=True)
    set = Column(Integer, nullable=True)
    is_secrecy = Column(Integer, nullable=True)
    popularity = Column(Integer, nullable=True)
    degree = Column(Integer, nullable=True)
    create_date = Column(DATETIME, nullable=True)
    create_by = Column(String(20), nullable=True)
    del_flag = Column(Integer, nullable=True)
    update_date = Column(DATETIME, nullable=True)
    update_by = Column(String(20), nullable=True)
    login_time = Column(DATETIME, nullable=False)
    ip = Column(String(30), nullable=False)
    post_address = Column(String(200), nullable=False)

