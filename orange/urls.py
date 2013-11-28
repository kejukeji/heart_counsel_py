# coding: UTF-8

from orange import app
from flask.ext import restful
from orange.controls.dingyue_control import *
from orange.controls.gls_category_control import *
from orange.controls.myf_archives_control import *
from orange.controls.index_control import *

#定义访问control路径
app.add_url_rule('/', 'index', show_index, methods={'GET', 'POST'})
app.add_url_rule('/dingyue', 'show_dingyue', show_dingyue, methods={'GET', 'POST'})
app.add_url_rule('/gls_category', 'show_gls_category', show_gls_category, methods={'GET', 'POST'})
app.add_url_rule('/self', 'show_myf_archives', show_myf_archives, methods={'GET', 'POST'})

api = restful.Api(app)

#定义接口路劲
# api.add_resource(ClassName, '/url')