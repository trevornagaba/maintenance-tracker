from flask_testing import TestCase
from run import app
import json

class MyTests(TestCase):
    
    def create_app(self):
        return app

    # Test the signup a user endpoint
    def test_signup(self):
        with self.client:
            post_data = (
                {
                    'username': 'bebeto',
                    'password': 'secret',
                    'reenter_password': 'secret'
                }
            )
            response = self.client.post(
                'v1/users/signup',
                content_type = 'application/json',
                data = json.dumps(post_data)
            )
            reply = json.loads(response.data.decode())
            self.assertEquals(reply['username'], 'bebeto')
            self.assertEquals(response.status_code, 201)
    # Test the login a user endpoint
    def test_login(self):
        with self.client:
            signup_data = (
                {
                    'username': 'bebeto',
                    'password': 'secret',
                    'reenter_password': 'secret'
                }
            )
            self.client.post(
                'v1/users/signup',
                content_type = 'application/json',
                data = json.dumps(signup_data)
            )
            login_data = (
                {
                    'username': 'bebeto',
                    'password': 'secret',
                }
            )
            response = self.client.post(
                'v1/users/login',
                content_type = 'application/json',
                data = json.dumps(login_data)
            )
            reply = json.loads(response.data.decode())
            self.assertEquals(reply['message'], 'User successfully logged in')
    
    # Test the create a request endpoint
    def test_create_requests(self):
        with self.client:
            post_data = (
                { 
                    "device_type":"laptop",
                    "fault_description": "Battery malfunctioning",
                    "device_status": "Submitted"
                }
            )
            response = self.client.post(
                '/v1/users/requests', 
                content_type = 'application/json', 
                data = json.dumps(post_data)
            )
            reply = json.loads(response.data.decode()) 
            self.assertTrue(reply['device-status'] in ['Submitted', 'Rejected', 'Approved', 'Resolved'], True)
            self.assertEquals(response.status_code, 201)

    # Test the view all requests endpoint
    def test_view_requests(self):
        with self.client:
            post_data = (
                { 
                    "device_type":"laptop",
                    "fault_description": "Battery malfunctioning",
                    "device_status": "Submitted"
                }
            )
            self.client.post(
                '/v1/users/requests', 
                content_type = 'application/json', 
                data = json.dumps(post_data)
            )            
            response = self.client.get(
                '/v1/users/requests',
                content_type = 'application/json'
            )
            reply = json.loads(response.data.decode())
            self.assertEquals(reply['number of requests'], 3) 
            self.assertEquals(reply['requests'][0]['id'], 1) 
            self.assertEquals(reply['message'], 'successful') 
            self.assertEquals(response.status_code, 200)

    # Test the view particular request endpoint
    def test_view_user_request(self):
        with self.client:
            post_data = (
                { 
                    "device_type":"laptop",
                    "fault_description": "Battery malfunctioning",
                    "device_status": "Submitted"
                }
            )
            self.client.post(
                '/v1/users/requests', 
                content_type = 'application/json', 
                data = json.dumps(post_data)
            )
            #remove content type
            response = self.client.get(
                '/v1/users/requests/1', 
                content_type = 'application/json'
            )
            reply = json.loads(response.data.decode()) 
            self.assertTrue(reply['device-status'] in ['Submitted', 'Rejected', 'Approved', 'Resolved'], True)
            self.assertEquals(reply['message'], 'successful')
            self.assertTrue(response.status_code, 200)

    # Test the modify a request endpoint
    def test_modify_request(self):
        with self.client:
            post_data = (
                { 
                    "device_type":"laptop",
                    "fault_description": "Battery malfunctioning",
                    "device_status": "Approved"
                }
            )
            put_data = (
                {
                    "device_type":"computer",
                    "fault_description": "Dead screen",
                    "device_status": "Submitted"
                }
            )
            self.client.post(
                '/v1/users/requests', 
                content_type = 'application/json', 
                data = json.dumps(post_data)
            )
            response = self.client.put(
                '/v1/users/requests/1', 
                content_type = 'application/json',
                data = json.dumps(put_data)
            )
            reply = json.loads(response.data.decode())
            self.assertTrue(reply['device-status'] in ['Submitted', 'Rejected', 'Approved', 'Resolved'], True)
            self.assertEquals(reply['device-type'], 'computer')
            self.assertEquals(response.status_code, 200)