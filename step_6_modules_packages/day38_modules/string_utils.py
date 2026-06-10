# string_utils.py

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def uppercase(s):
    return s.upper()

def lowercase(s):
    return s.lower()

def word_count(s):
    return len(s.split())