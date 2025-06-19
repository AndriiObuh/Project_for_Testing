import pytest
import sqlite3
from unittest.mock import Mock

@pytest.fixture
def sample_file(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello pytest\nSecond line")
    return file_path

@pytest.fixture
def sample_user():
    return {
        "username": "andrii",
        "email": "andrii@example.com",
        "role": "admin",
        "active": True
    }

@pytest.fixture
def mock_api_response():
    mock = Mock()
    mock.status_code = 200
    mock.json.return_value = {"message": "Success", "data": [1, 2, 3]}
    return mock

@pytest.fixture
def db_conn():
    conn = sqlite3.connect(":memory:")  # БД в оперативній пам’яті
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")
    cursor.execute("INSERT INTO users VALUES (1, 'Andrii')")
    cursor.execute("INSERT INTO users VALUES (2, 'Vika')")
    conn.commit()
    yield conn
    conn.close()
