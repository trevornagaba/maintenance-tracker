from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/users/requests', methods = ['GET'])
def view_requests():
    return jsonify({'status_code':'200', 'message':'successful'})

@app.route('/users/requests', methods = ['POST'])
def create_requests():
    return jsonify({ 'device-type':'laptop','fault-description': 'Battery malfunctioning'})

@app.route('/users/requests/requestId', methods = ['GET'])
def view_user_requests():
    return jsonify({'status_code':'200', 'message': 'successful'})

@app.route('/users/request/requestId', methods = ['PUT'])
def modify_requests():
    return jsonify({'device-type':'phone', 'fault-description':'Screen cracked'})

if __name__ == '__main__':
    app.run()