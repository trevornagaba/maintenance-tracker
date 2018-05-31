from flask import Flask, request, jsonify
from models import Request
import json

# A list to store requests
requests = []

app = Flask(__name__)

#Create a request
@app.route('/v1/users/requests', methods = ['POST'])
def create_requests():
    # Retrieve the data
    data = request.get_json()
    # Validate the data
    try:
        if isinstance(data['device_type'].encode(), str) and isinstance (data['fault_description'].encode(), str) and isinstance (data['device_status'].encode(), str):
            # Create id and store the data
            id = len(requests) + 1
            req =  Request(id, data['device_type'], data['fault_description'], data['device_status'])
            requests.append(req)
            return jsonify(
                {
                    'status':'OK',
                    'message': 'Request created successfully',
                    'id': id,
                    'device-status': requests[id-1].get_device_status(),
                    'device-type': requests[id-1].get_device_type()
                }
            ), 201
    except AttributeError:
        return jsonify(
            {
                'status':'FAILED',
                'message': 'Invalid request',
            }
        ), 400

#Fetch all requests of a logged in user
@app.route('/v1/users/requests', methods = ['GET'])
def view_requests():
        return jsonify(
                {
                'status':'OK', 
                'message':'successful',
                'requests': [json.dumps(a_request.__dict__) for a_request in requests]
                }
            ), 201

#Fetch a request that belongs to a logged in user
@app.route('/v1/users/requests/<id>', methods = ['GET'])
def view_user_requests(id):
    # Convert id to integer 
    id_number = int(id)
    # Validate request
    try: 
        if isinstance(id_number, int):
            return jsonify(
                {
                'status':'OK', 
                'message':'successful',
                'device-type': requests[id_number-1].get_device_type(),
                'fault description': requests[id_number-1].get_fault_description(),
                'device-status': requests[id_number-1].get_device_status(),
                'id': requests[id_number-1].id
                }
            ), 201
    except  ValueError:
        return jsonify(
            {
                'status':'FAILED',
                'message':'Invalid request id'
            }
        ), 400
    except IndexError:
        return jsonify(
            {
                'status':'FAILED',
                'message':'Your request id does not exist'
            }
        ), 400

#Modify a request
@app.route('/v1/users/requests/<id>', methods = ['PUT'])
def modify_requests(id):
    # 1. Capture data from the request
    data = request.get_json()
    id_number = int(id)
    # 2. validate the data
    try:
        if isinstance(data['device_type'].encode(), str) and isinstance(data['fault_description'].encode(), str) and isinstance(data['device_status'].encode(), str)and isinstance(id_number, int):
            # 3. Store the data 
            requests[id_number-1].device_type = data['device_type'].encode()
            requests[id_number-1].fault_description = data['fault_description'].encode()
            requests[id_number-1].device_status = data['device_status'].encode()

            return jsonify(
                {
                'status': 'OK',
                'device-type': requests[id_number-1].get_device_type(),
                'fault-description': requests[id_number-1].get_fault_description(),
                'message': 'A request was modified',
                'request-id': id,
                'device-status': requests[id_number-1].get_device_status()
                }
            ), 201
    except AttributeError:
        return jsonify(
            {
            'status': 'FAIL',
            'message': 'Failed to modify a request. Data is invalid'
            }
        ), 400
    except IndexError:
        return jsonify(
            {
            'status': 'FAIL',
            'message': 'Request id out of range'
            }
        ), 400


if __name__ == '__main__':
    app.run(debug = 'True')   