# coding: UTF-8
from orange.models.gls_epilog import Gls_epilog as Gls_epilog


def get_gls_epilog():
    gls_epilog = Gls_epilog.query.filter().all()
    return gls_epilog

