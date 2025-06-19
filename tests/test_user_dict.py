def test_user_name(sample_user):
    assert sample_user["username"] == "andrii"

def test_user_role(sample_user):
    assert sample_user["role"] == "admin"

def test_user_is_active(sample_user):
    assert sample_user["active"] is True