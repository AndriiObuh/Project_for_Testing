from app.main import is_even, get_max, is_palindrome
import pytest


@pytest.mark.parametrize(
    "number, expected",
    [
        (4, True),
        (5, False),
        (0, True),
        (-2, True),
        (-3, False),
    ]
)
def test_even_number(number, expected):
    assert is_even(number) == expected


@pytest.mark.parametrize(
    "my_lst, expected",
    [
        ([1, 2, 3], 3),
        ([5, 2, 10, 4], 10),
        ([-5, -3, -8, -4, -14], -3),
        ([-5, -5, 8, 8, 2], 8),
        ([42], 42),
    ]
)
def test_get_max(my_lst, expected):
    assert get_max(my_lst) == expected


def test_get_max_empty_list():
    with pytest.raises(ValueError):
        get_max([])


@pytest.mark.parametrize(
    "text, expected",
    [
        ("radar", True),
        ("hello", False),
        ("", True),
        ("Aibohphobia", True),
        ("A man a plan a canal Panama", True),
        ("12321", True),
    ]
)
def test_palindrome_simple(text, expected):
    assert is_palindrome(text) == expected
