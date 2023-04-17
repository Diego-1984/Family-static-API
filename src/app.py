"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():
    pass

@app.route('/member/<int:member_id>', methods=['GET'])
def get_specific_member(id):
    pass

@app.route('/member', methods=['POST'])
def add_member():
    request_data = request.get_json()
    first_name = request_data.get('first_name')
    age = request_data.get('age')
    lucky_numbers = request_data.get('lucky_numbers', [])
    member_id = request_data.get('id')
    
    # Código para agregar el miembro de la familia
    
    return {
        'message': 'Miembro agregado con éxito',
        'data': {
            'first_name': first_name,
            'age': age,
            'lucky_numbers': lucky_numbers,
            'id': member_id
        }
    }


@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    return {
        'message': 'Miembro agregado con éxito',
            body: {
            done: True
}
    }

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "hello": "world",
        "family": members
    }


    return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
