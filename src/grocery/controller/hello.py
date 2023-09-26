from flask import Blueprint

blueprint = Blueprint('hello_blueprint', __name__)


# http://localhost:8081/hello
@blueprint.route("/hello", methods=["GET"])
def hello():
    return "Hello World!"
