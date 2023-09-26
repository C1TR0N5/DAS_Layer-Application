from flask import Flask
from grocery.controller import handlers
from grocery.controller import hello

app = Flask(__name__)
app.register_blueprint(handlers.blueprint)
app.register_blueprint(hello.blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)
