def is_palindrome(s):
    if len(s) <= 1:
        return True
    
    s = ''.join(char.lower() for char in s if char.isalnum())

    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

print(is_palindrome("radar"))       # Output: True
print(is_palindrome("Able was I ere I saw Elba"))  # Output: True
print(is_palindrome("hello"))        # Output: False
