#!/usr/bin/python3
""" Indexing"""

import models
from models.user import User
from models.settings import Settings
from models.data import Data
from models import storage
from api.v1.blueprints import app_views
from flask import jsonify

strict_slashes=False

@app_views.route('/status', methods=['GET'])
def status():
    """ status of APIA """
    return jsonify({'Status': 'OK'})

@app_views.route('/numbers', methods=['GET'])
def num_objects():
    """ retrieves number of each objct by type """
    classes = [User, Settings, Data]
    names = ["users", "settings", "datas"]

    num_objcts = {}
    for i in range(len(classes)):
        num_objcts[names[i]] = storage.count(classes[i])

    return jsonify(num_objcts)
