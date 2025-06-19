def test_user_exists(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT name FROM users WHERE id = 1")
    result = cursor.fetchone()
    assert result[0] == "Andrii"

def test_user_count(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    result = cursor.fetchone()
    assert result[0] == 2


