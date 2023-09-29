'''
from flask import Flask
from grocery.controller import handlers
from grocery.controller import hello

app = Flask(__name__)
app.register_blueprint(handlers.blueprint)
app.register_blueprint(hello.blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)
'''

from flask import Flask, jsonify, request, abort
import pandas as pd

app = Flask(__name__)

# Load the CSV file into memory as a DataFrame
data_source = pd.read_csv("src/grocery/repository/sample_grocery.csv")


@app.route('/item', methods=['GET'])
def get_items():
    return jsonify(data_source.to_dict(orient='records'))


@app.route('/item', methods=['POST'])
def add_item():
    """ SKU,Name,Description,Price,Quantity,Expiration Date """
    item = {
        'SKU': request.json.get('SKU', ""),
        'Name': request.json.get('Name', ""),
        'Description': request.json.get('Description', ""),
        'Price': request.json.get('Price', 0.0),
        'Quantity': request.json.get('Quantity', 0),
        'Expiration Date': request.json.get('Expiration Date', "")
    }
        
    data_source.append(item, ignore_index=True)
    return jsonify(item), 201


@app.route('/item/<string:SKU>', methods=['DELETE'])
def delete_item(SKU):
    global data_source
    data_source = data_source[data_source.SKU != SKU]
    return jsonify({"result": "success"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)
