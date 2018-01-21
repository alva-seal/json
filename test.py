import unittest
import requests
from main import app


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello(self):
        response = self.app.get('/')
        self.assertEqual(response.data.decode(), "Hello World from Python!")


if __name__ == "__main__":
    unittest.main()
