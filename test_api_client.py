from unittest import TestCase
from unittest.mock import patch, MagicMock


from api_client import ApiClient


class TestApiClient(TestCase):

    @patch('api_client.requests.get')
    def test_get_comments(self, mock_requests_get):

        expected = [
            {'id': 2, 'body': 'some comment', 'postId': 2},
            {'id': 3, 'body': 'some comment', 'postId': 2}
        ]

        mock_response = MagicMock()
        mock_response.json.return_value = expected

        mock_requests_get.return_value = mock_response

        r = ApiClient().get_comments()

        self.assertEqual(r, expected)
        
