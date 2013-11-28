# coding: UTF-8
from orange.models.myf_archives import Myf_archives as Myf_archives


def get_myf_archives_self():
    count = Myf_archives.query.filter(Myf_archives.typename == '自我的秘密').count()
    if count == 1:
        myf_archives_self = Myf_archives.query.filter(Myf_archives.typename == '自我的秘密')
    else:
        myf_archives_self = Myf_archives.query.filter(Myf_archives.typename == '自我的秘密').all()


    return myf_archives_self

