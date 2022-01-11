from utils.main_funtions import *

class TestTimezone(unittest.TestCase):
    def setUp(self):
        self.header = {'Authorization': auth_token()}

    def test_get_timezone(self):
        response = requests.get(f"{URL}/user-profile", headers=self.header)
        assert_equal(response.status_code, 200)

        json_data = json.loads(response.content)
        lang = json_data['languages']
        timez = json_data['timezones']

        port = lang[0]
        assert_in("id", port)
        assert_equal(type(port['id']), int)
        assert_equal(port['id'], 1)

        assert_in("name", port)
        assert_equal(type(port['name']), str)
        assert_equal(port['name'], "Português")

        assert_in("code", port)
        assert_equal(type(port['code']), str)
        assert_equal(port['code'], "pt")

        eng = lang[1]
        assert_in("id", eng)
        assert_equal(type(eng['id']), int)
        assert_equal(eng['id'], 2)

        assert_in("name", eng)
        assert_equal(type(eng['name']), str)
        assert_equal(eng['name'], "English")

        assert_in("code", eng)
        assert_equal(type(eng['code']), str)
        assert_equal(eng['code'], "en")

        esp = lang[2]
        assert_in("id", esp)
        assert_equal(type(esp['id']), int)
        assert_equal(esp['id'], 3)

        assert_in("name", esp)
        assert_equal(type(esp['name']), str)
        assert_equal(esp['name'], "Español")

        assert_in("code", esp)
        assert_equal(type(esp['code']), str)
        assert_equal(esp['code'], "es")

        for timezones in timez:
            assert_in("id", timezones)
            assert_equal(type(timezones['id']), int)

            assert_in("name", timezones)
            assert_equal(type(timezones['name']), str)

            assert_in("timeAdjustment", timezones)
            assert_equal(type(timezones['timeAdjustment']), str)

            assert_in("active", timezones)
            assert_equal(type(timezones['active']), bool)
