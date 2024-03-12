import sys

def is_palindrome(s):
    ret = False
    if len(s) <= 0:
        print("invalid argment")
        return ret
    argReversed = ""
    temp = len(s) - 1
    for num in range(len(s)):
        argReversed += s[temp]
        temp -= 1
    if s.lower() == argReversed.lower():
        ret = True

    return ret

print(is_palindrome("radar"))       # Output: True
print(is_palindrome("Able was I ere I saw Elba"))  # Output: True
print(is_palindrome("hello"))        # Output: False

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python test.py <string>")
#     else:
#         try:
#             sentence = str(sys.argv[1])
#             print(is_palindrome(sentence))
#         except ValueError:
#             print("Invelid input. Please provide a string.")