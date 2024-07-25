import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')
        
    def test_semantic_release(self):
        tester = app.test_client(self)
        response = tester.get('/semantic-release')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Semantic Release')

    def test_other_route(self):
        tester = app.test_client(self)
        response = tester.get('/other')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Other Route')

if __name__ == '__main__':
    unittest.main()

