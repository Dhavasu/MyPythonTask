def to_uppercase(s):
    upper = s.upper()
    print(f"Uppercase: {upper}")
    return upper

def to_lowercase(s):
    lower = s.lower()
    print(f"Lowercase: {lower}")
    return lower

def reverse_string(s):
    reverse = s[::-1]
    print(f"Reversed: {reverse}")
    return reverse

def is_palindrome(s):
    palindrome = s == s[::-1]  
    print(f"Is Palindrome: {palindrome}")
    return palindrome 

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in s if char in vowels)
    print(f"Vowel count: {vowel_count}")
    return vowel_count
