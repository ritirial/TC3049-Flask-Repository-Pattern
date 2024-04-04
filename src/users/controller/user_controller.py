from flask import Blueprint, jsonify, request
from users.model.user_model import User
from users.repository.user_repository import UserRepository, LocalUserRepository


blueprint = Blueprint('user_controller', __name__)
#users = [] ya inicializado en repository

repository = LocalUserRepository()

# Endpoint to insert users
@blueprint.route("/users", methods=["POST"])
def insert_user():
    # Get the user data from the request
    user_data = request.get_json()

    # Add the new user to the list of repository of users
    user = repository.add(user_data["name"], user_data["email"])

    # Return the newly inserted user
    return jsonify(user)


# Endpoint to retrieve users based on user_id
@blueprint.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):

    # Find the user with the given user_id in repository
    id = int(user_id)
    user = repository.get(id)

    # If the user is not found, return a 404 error
    if user is None:
        return jsonify({"message": "User not found"}), 404

    # Return the retrieved user
    return jsonify(user)