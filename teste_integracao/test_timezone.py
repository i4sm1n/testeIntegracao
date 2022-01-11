from utils.main_funtions import *

class TestTimezone(unittest.TestCase):
    def setUp(self):
        self.header = {'Authorization': auth_token()}

    def test_get_timezone(self):
        response = requests.get(f"{URL}/timezone", headers=self.header)
        assert_equal(response.status_code, 200)

        json_data = json.loads(response.content)

        for info in json_data:
            assert_in("id", info)
            assert_equal(type(info['id']), int)

            assert_in("name", info)
            assert_equal(type(info['name']), str)

            assert_in("timeAdjustment", info)
            assert_equal(type(info['timeAdjustment']), str)

            assert_in("active", info)
            assert_equal(type(info['active']), bool)