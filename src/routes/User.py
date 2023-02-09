from flask import Blueprint, jsonify

main = Blueprint("user_blueprint", __name__)

@main.route('/')
def getUsers():
    return jsonify({"message":"GabyCliff"})