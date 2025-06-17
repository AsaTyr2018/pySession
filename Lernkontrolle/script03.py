def reverse_string(s):
    return s[::-1]

"""Return the string reversed."""

def is_palindrome(s):
    return s == s[::-1]
"""Check if the string is a palindrome."""


def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for c in s if c in vowels)
