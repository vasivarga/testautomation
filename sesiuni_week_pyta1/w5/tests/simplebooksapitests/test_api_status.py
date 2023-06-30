import unittest

from w5.requests.simplebooksapi.simple_books_requests import SimpleBooksRequests


class TestApiStatus(unittest.TestCase):

    def setUp(self):
        self.books_api = SimpleBooksRequests()

    def test_api_status(self):
        response = self.books_api.get_api_status()

        expected_response_code = 200
        actual_response_code = response.status_code

        self.assertEqual(expected_response_code, actual_response_code, "Error, unexpected status code")

        expected_response_message = "OK"
        actual_response_message = response.json()["status"]

        self.assertEqual(expected_response_message, actual_response_message, "Error, unexpected response message")