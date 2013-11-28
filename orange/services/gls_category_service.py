# coding: UTF-8
from orange.models.gls_category import Gls_category as Gls_category


def get_gls_category():
    gls_category = Gls_category.query.filter().all()
    return gls_category

