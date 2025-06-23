import pytest
from unittest.mock import patch, Mock
from app.api_client import APIClient

@pytest.fixture
def client():
    return APIClient()

def test_get_post_success(client):
    """ Post list return test """
    with patch ("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"id": 1, "title": "Test post"}]
        mock_get.return_value = mock_response

        posts = client.get_posts()
        assert isinstance(posts, list)
        assert posts[0]["id"] == 1

def test_get_post_found(client):
    """ Post finding test by ID """
    with patch ("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": 1, "title": "One post"}
        mock_get.return_value = mock_response

        post = client.get_post(1)
        assert post["id"] == 1

def test_get_post_not_found(client):
    """Test if post not found (404)"""
    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        post = client.get_post(999)
        assert post is None

