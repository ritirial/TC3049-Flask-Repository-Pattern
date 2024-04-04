from flask import Blueprint, jsonify, request
from courses.repository.course_repository import LocalCourseRepository


blueprint = Blueprint('user_controller', __name__)

repository = LocalCourseRepository()

# Endpoint to insert course
@blueprint.route("/courses", methods=["POST"])
def insert_course():
    # Get the course data from the request
    item_data = request.get_json()

    # Send request data to repository and attempt to add a new course 
    course = repository.add(item_data["name"], item_data["description"])
    
    # If repository.add() returned None, course name already used
    if course is None:
        return jsonify({"message": "Course already exists"}), 404
    
    # Return the newly inserted user
    return jsonify(course)


# Endpoint to retrieve courses based on id
@blueprint.route("/courses/<course_id>", methods=["GET"])
def get_course(course_id):

    # Find the course with the given id in repository
    course = repository.get(int(course_id))

    # If the course is not found, return a 404 error
    if course is None:
        return jsonify({"message": "Course not found"}), 404

    # Return the retrieved course
    return jsonify(course)