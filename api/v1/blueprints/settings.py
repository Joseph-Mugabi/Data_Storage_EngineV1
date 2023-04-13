#!/usr/bin/pyyhon3
""" objcts  to handle all default RestFul API actions for settings """

from models.settings import Settings
from models.user import User
from models import storage
from api.v1.blueprints import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

strict_slashes = False
@app_views.route('/users/user_id/settings', methods=['GET'])
@swag_from('documentation/setting/settings_by_user.yml')
def get_settings():
    """ Retrieves the list of all setting objects of specific user """
    user = storage.get(User, user_id)
    list_of_settings = []
    if not user:
        abort(404)
    for setting in user.settings:
        list_of_settings.append(setting.to_dict())
    return jsonify(list_of_settings.to_dict())

@app_views.route('/settings/<setting_id>', methods=['GET'])
@swag_from('documentation/setting/get_setting.yml', methods=['GET'])
def get_setting(setting_id):
    """retrieving setting """
    setting = storage.get( Settings, setting_id)
    if setting:
        return jsonify(setting.to_dict())
    else:
        abort(404)

@app_views.route('/settings', methods=['POST'])
@swag_from('documentation/setting/post_setting.yml', methods=['POST'])
def post_setting():
    """ create setting """
    setting = request.json
    if not setting:
        abort(400, ddescription="Not a JSON")
    data = Settings(**setting)
    data.save()
    return make_response(jsonify(data.to_dict()), 201)

@app_views.route('/settings/<setting_id>', methods=['PUT'])
@swag_from('documentation/setting/put_setting.yml', methods=['PUT'])
def put_setting(setting_id):
    """ update a setting """
    setting = storage.get(Settings, setting_id)
    obj = request.json
    if not setting:
        abort(404)
    if not obj:
        abort(400, description='Not a JSON')

    ignore = ['id',' user_id', 'created_at', 'updated_at']
    for key, value in obj.items():
        if key not in ignore:
            setattr(setting, key, value)
    storage.save()
    return make_response(jsonify(setting.to_dict()), 200)

@app_views.route('/settings/<setting_id>', methods=['DELETE'])
@swag_from('documentation/setting/delete_setting.yml', methods=['DELETE'])
def del_setting(settting_id):
    """ deletes a setting object """
    setting = storage.get(Settings, setting_id)
    if not setting:
        abort(404)

    storage.delete(data)
    storage.save()
    return make_response(jsonify({}), 200)
