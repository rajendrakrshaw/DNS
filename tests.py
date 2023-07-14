import unittest
import json
from main import app


class DNSHandlerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_dns_handler(self):
        data = {
            "x": "123.12",
            "y": "456.56",
            "z": "789.89",
            "vel": "20.0"
        }

        response = self.app.post('/dns', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        response_data = json.loads(response.data)
        self.assertIn('loc', response_data)
        self.assertAlmostEqual(response_data['loc'], 1389.57, places=2)

    def test_dns_handler_invalid_data(self):
        data = {
            "x": "abc",  # Invalid value
            "y": "456.56",
            "z": "789.89",
            "vel": "20.0"
        }

        response = self.app.post('/dns', json=data)
        self.assertEqual(response.status_code, 500)

    def test_dns_handler_missing_fields(self):
        data = {
            "x": "123.12",
            "z": "789.89",
            "vel": "20.0"
        }

        response = self.app.post('/dns', json=data)
        self.assertEqual(response.status_code, 500)

    def test_dns_handler_negative_values(self):
        data = {
            "x": "-123.12",
            "y": "456.56",
            "z": "789.89",
            "vel": "20.0"
        }

        response = self.app.post('/dns', json=data)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn('loc', response_data)
        self.assertAlmostEqual(response_data['loc'], 1143.33, places=2)

    def test_dns_handler_zero_values(self):
        data = {
            "x": "0",
            "y": "0",
            "z": "0",
            "vel": "0"
        }

        response = self.app.post('/dns', json=data)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn('loc', response_data)
        self.assertAlmostEqual(response_data['loc'], 0, places=2)

    def test_dns_handler_large_values(self):
        data = {
            "x": "1000000000.0",
            "y": "2000000000.0",
            "z": "3000000000.0",
            "vel": "1000000.0"
        }

        response = self.app.post('/dns', json=data)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn('loc', response_data)
        self.assertAlmostEqual(response_data['loc'], 6001000000.0, places=2)

    #add more test cases

if __name__ == '__main__':
    unittest.main()
