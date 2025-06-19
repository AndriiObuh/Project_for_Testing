def test_mocked_status_code(mock_api_response):
    assert mock_api_response.status_code == 200

def test_mock_json(mock_api_response):
    data = mock_api_response.json()
    assert data["message"] == "Success"
    assert data["data"] == [1, 2, 3]
