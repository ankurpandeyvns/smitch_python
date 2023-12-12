import requests
import functools


def catch_exception(f):
    @functools.wraps(f)
    def func(*args, **kwargs):
        return f(*args, **kwargs)
    return func


class InvalidAPIKeyError(Exception):
    def __init__(self):
        super().__init__('The API Key you passed is invalid!')


class Smitch:
    def __init__(self, api_key):
        self.base_url = 'https://app.api.developer.mysmitch.com/v1/app/'
        self.headers = {
            'accept': 'application/json',
            'x-api-key': api_key,
            'Content-Type': 'application/json'
        }
        api_key_valid_response = self.get('details')
        if 'status' not in api_key_valid_response or api_key_valid_response['status'] != 'success':
            raise InvalidAPIKeyError

    def get(self, url, params=None):
        if params is None:
            params = {}
        return requests.get(self.base_url + url, headers=self.headers, params=params).json()

    def post(self, url, post_data=None):
        if post_data is None:
            post_data = {}
        return requests.post(self.base_url + url, headers=self.headers, json=post_data).json()

    @catch_exception
    def users(self):
        return self.get('users')['data']

    @catch_exception
    def user(self, user_id):
        if 'data' in self.get('user', {'user_id': user_id}):
            return SmitchUser(self, user_id)
        print('User not found!')


class SmitchUser:
    def __init__(self, client, user_id):
        self.client = client
        self.user_id = user_id

    @catch_exception
    def devices(self):
        return self.client.get('user', {'user_id': self.user_id})['data'][0]['user_devices']

    @catch_exception
    def device(self, device_id):
        if 'data' in self.client.get('device/details', {'user_id': self.user_id, 'device_id': device_id}):
            return SmitchDevice(self.client, self.user_id, device_id)
        print('Invalid Device ID!')

    @catch_exception
    def device_details(self, device_id):
        response = self.client.get('device/details', {'user_id': self.user_id, 'device_id': device_id})
        if 'data' in response:
            return response['data']
        print('Invalid Device ID!')


class SmitchDevice:
    def __init__(self, client, user_id, device_id):
        self.payload = {
            "user_id": user_id,
            "commands": [
                {
                    "device_id": device_id,
                }
            ]
        }
        self.client = client
        self.user_id = user_id
        self.device_id = device_id

    def name(self):
        return self.client.get('device/details', {'user_id': self.user_id, 'device_id': self.device_id})['data']['name']
        
    def change_state(self, state, rgb=None):
        self.payload['commands'][0]['device_settings'] = {
                        "power_status": state
                    }
        if rgb:
            self.payload['commands'][0]['device_settings']['colour'] = {
                'r': rgb[0],
                'g': rgb[1],
                'b': rgb[2]
            }
        response = self.client.post('job/device', self.payload)
        if 'status' in response and response['status'] == 'success':
            print('Device Turned', 'ON!' if state else 'OFF!')
        else:
            print('Some Error Occurred!')

    def on(self, rgb=None):
        if rgb:
            self.change_state(True, rgb)
        else:     
            self.change_state(True)        

    def off(self):
        self.change_state(False)
