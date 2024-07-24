import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_new_one(self):
        tester = app.test_client(self)
        response = tester.get('/new-one')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'a whole new world!')

if __name__ == '__main__':
    unittest.main()
