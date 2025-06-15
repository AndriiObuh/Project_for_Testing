def is_even(n):
    return n % 2 == 0

def get_max(numbers):
    if not numbers:
        raise ValueError("List is empty")
    return max(numbers)

def is_palindrome(s):
    cleaned = ''.join(s.lower().split())
    return cleaned == cleaned[::-1]
