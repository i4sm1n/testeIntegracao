import json
import unittest
import requests
from nose.tools import *


URL = "https://testapi.jasgme.com/sgme/api"

def auth_token():
    data = {
        "login": "iasmin.santos@dellead.com",
        "password": "1234abcd"
    }

    response = requests.post(f"{URL}/authenticate/login", json=data)
    assert_equal(response.status_code, 200)

    json_data = json.loads(response.content)
    token = json_data['token']
    return f"Bearer {token}"