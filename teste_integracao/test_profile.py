import unittest
import requests
import json
from utils.main_funtions import *

class TestProile(unittest.TestCase):
    def setUp(self):
        self.header = {'Authorization': auth_token()}

    def test_get_profile(self):
        response = requests.get(f"{URL}/profiles", headers=self.header)
        assert_equal(response.status_code, 200)

        json_data = json.loads(response.content)

        #baixa mutabilidade
        adm = json_data[0]
        assert_in("id", adm)
        assert_equal(type(adm['id']), int)
        assert_equal(adm['id'], 1)

        assert_in("name", adm)
        assert_equal(type(adm['name']), str)
        assert_equal(adm['name'], "Administrator")

        assert_in("type", adm)
        assert_equal(type(adm['type']), str)
        assert_equal(adm['type'], "ADMINISTRATOR")

        ach = json_data[1]
        assert_in("id", ach)
        assert_equal(type(ach['id']), int)
        assert_equal(ach['id'], 2)

        assert_in("name", ach)
        assert_equal(type(ach['name']), str)
        assert_equal(ach['name'], "Achiever")

        assert_in("type", ach)
        assert_equal(type(ach['type']), str)
        assert_equal(ach['type'], "ACHIEVER")

        adv = json_data[2]
        assert_in("id", adv)
        assert_equal(type(adv['id']), int)
        assert_equal(adv['id'], 3)

        assert_in("name", adv)
        assert_equal(type(adv['name']), str)
        assert_equal(adv['name'], "Adviser")

        assert_in("type", adv)
        assert_equal(type(adv['type']), str)
        assert_equal(adv['type'], "ADVISER")

        coor = json_data[3]
        assert_in("id", coor)
        assert_equal(type(coor['id']), int)
        assert_equal(coor['id'], 4)

        assert_in("name", coor)
        assert_equal(type(coor['name']), str)
        assert_equal(coor['name'], "Coordinator")

        assert_in("type", coor)
        assert_equal(type(coor['type']), str)
        assert_equal(coor['type'], "COORDINATOR")
        pass
