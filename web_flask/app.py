#!/usr/bin/python3
"""populate the view"""

from flask import Flask, jsonify, request
from models import storage
from models.user import User

app = Flask(__name__)

# List all users
@app.route('/users', methods=['GET'])
def get_users():
    users = storage.all(User)
    return jsonify([user.to_dict() for user in users.values()])

# Get a specific user by id
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict())

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing required field'}), 400
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201

# Update an existing user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    data = request.get_json()
    for key, value in data.items():
        setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict())

# Delete a user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = storage.get(User, user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    user.delete()
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
