#!/usr/bin/pyyhon3
""" objcts  to handle all default RestFul API actions for users """

from models.data import Data
from models import storage
from api.v1.blueprints import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

strict_slashes = False
@app_views.route('/datas', methods=['GET'])
@swag_from('documentation/data/get_data.yml')
def get_datas():
    """ Retrieves the list of all data objects """
    all_datas = storage.all(Data).values()
    list_of_datas = []
    for data in all_datas:
        list_of_datas.append(data.to_dict())
    return jsonify(list_of_datas)

@app_views.route('/datas/<string:id>', methods=['GET'])
@swag_from('documentation/date/get_id_user.yml', methods=['GET'])
def get_data(data_id):
    """retrieving data"""
    data = storage.get(Data, data_id)
    if data:
        return jsonify(data.to_dict())
    else:
        abort(404)

@app_views.route('/datas', methods=['POST'])
@swag_from('documentation/data/post_data.yml', methods=['POST'])
def post_data():
    """ create data """
    data = request.json
    if not data:
        abort(400, ddescription="Not a JSON")
    p_data = Data(**data)
    p_data.save()
    return make_response(jsonify(p_data.to_dict()), 201)

@app_views.route('/datas/<data_id>', methods=['PUT'])
@swag_from('documentation/data/put_data.yml', methods=['PUT'])
def put_data(data_id):
    """ update a data """
    data_obj = storage.get(Data, data_id)
    obj = request.json
    if not data_obj:
        abort(404)
    if not obj:
        abort(400, description='Not a JSON')

    ignore = ['id', 'created_at', 'updated_at']
    for key, value in obj.items():
        if key not in ignore:
            setattr(data_obj, key, value)
    storage.save()
    return make_response(jsonify(data_obj.to_dict()), 200)

@app_views.route('/datas/<data_id>', methods=['DELETE'])
@swag_from('documentation/data/delete_data.yml', methods=['DELETE'])
def del_data(data_id):
    """ deletes a data object """
    data = storage.get(Data, data_id)
    if not data:
        abort(404)

    storage.delete(data)
    storage.save()
    return make_response(jsonify({}), 200)
