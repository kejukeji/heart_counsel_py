# coding: UTF-8
from orange.models.dingyue import Dingyue as DingYue


def get_dingyue():
    dingyue = DingYue.query.filter().all()
    return dingyue

