def test_read_file(sample_file):
    with open(sample_file, "r") as f:
        content = f.read()
    assert "pytest" in content
    assert  "Second" in content