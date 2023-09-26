from flask import Blueprint, jsonify
from grocery.repository import data

blueprint = Blueprint('my_blueprint', __name__)
grocery_data = data.load_sample_data()


# http://localhost:8081/mario
@blueprint.route("/name/<name>", methods=["GET"])
def root(name: str):
    return f"Hello {name}"


@blueprint.route('/json', methods=["GET"])
def json():
    return jsonify(grocery_data)