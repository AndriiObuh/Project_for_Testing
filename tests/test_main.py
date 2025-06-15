from app.main import is_even, get_max, is_palindrome
import pytest


def test_even_number():
    assert is_even(4) == True


def test_odd_number():
    assert is_even(5) == False


def test_zero():
    assert is_even(0) == True


def test_negative_even():
    assert is_even(-2) == True


def test_negative_odd():
    assert is_even(-3) == False


def test_get_max_positive_numbers():
    assert get_max([1, 5, 3, 9, 2]) == 9


def test_get_max_negative_numbers():
    assert get_max([-10, -5, -3]) == -3


def test_get_max_mixed_numbers():
    assert get_max([-2, 0, 7, 4]) == 7


def test_get_max_single_element():
    assert get_max([42]) == 42


def test_get_max_empty_list():
    with pytest.raises(ValueError):
        get_max([])


def test_palindrome_simple():
    assert is_palindrome("madam") == True


def test_palindrome_with_spaces():
    assert is_palindrome("nurses run") == True


def test_palindrome_mixed_case():
    assert is_palindrome("RaceCar") == True


def test_not_palindrome():
    assert is_palindrome("hello") == False


def test_empty_string():
    assert is_palindrome("") == True  # порожній рядок вважаємо паліндромом


def test_palindrome_with_upper_and_spaces():
    assert is_palindrome("A man a plan a canal Panama") == True
