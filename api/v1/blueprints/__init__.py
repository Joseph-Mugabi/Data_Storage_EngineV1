#!/usr/bin/python3
""" blueprint for API """

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.blueprints.index import *
from api.v1.blueprints.users import *
from api.v1.blueprints.settings import *
from api.v1.blueprints.datas import *

