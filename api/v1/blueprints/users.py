#!/usr/bin/pyyhon3
""" objcts  to handle all default RestFul API actions for users """

from models.user import User
from models import storage
from api.v1.blueprints import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

strict_slashes = False
@app_views.route('/users', methods=['GET'])
@swag_from('documentation/user/all_user.yml')
def get_users():
    """Retrieves the list of all user objects
        or a specific user
    """
    all_users = storage.all(User).values()
    list_of_users = []
    for user in all_users:
        list_of_users.append(user.to_dict())
    return jsonify(list_of_users)

@app_views.route('/users/<string:id>', methods=['GET'])
@swag_from('documentation/user/get_user.yml', methods=['GET'])
def get_user(id):
    """retrieving user"""
    user = storage.get(User, id)
    if user:
        return jsonify(user.to_dict())
    else:
        abort(404)

@app_views.route('/users', methods=['POST'])
@swag_from('documentation/user/post_user.yml', methods=['POST'])
def post_user():
    """ create user """
    data = request.json
    if not data:
        abort(400, ddescription="Not a JSON")
    if 'email' not in data:
        abort(400, description="Missing AN Email")
    if 'password' not in data:
        abort(400, description='Missing Password')
    user = User(**data)
    user.save()
    return make_response(jsonify(user.to_dict()), 201)

@app_views.route('/users/<user_id>', methods=['PUT'])
@swag_from('documentation/user/put_user.yml', methods=['PUT'])
def put_user(user_id):
    """ update a user """
    user = storage.get(User, user_id)
    data = request.json
    if not user:
        abort(404)
    if not data:
        abort(400, description='Not a JSON')
    ignore = ['id', 'email', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)

@app_views.route('/users/<user_id>', methods=['DELETE'])
@swag_from('documentation/user/delete_user.yml', methods=['DELETE'])
def del_user(user_id):
    """ deletes a user object """
    user = storage.get(User, user_id)
    if not user:
        abort(404)

    storage.delete(user)
    storage.save()
    return make_response(jsonify({}), 200)
