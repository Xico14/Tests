import unittest
import re
from auth_yandex_id import wait_element, auth_func

class TestAuthYandexId(unittest.TestCase):

    def test_email_input_regex(self):
        valid_email = 'test@example.com'
        invalid_email = 'invalid_email'
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        self.assertTrue(re.match(email_pattern, valid_email))
        self.assertFalse(re.match(email_pattern, invalid_email))

if __name__ == '__main__':
    unittest.main()