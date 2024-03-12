import sys

def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        print("Argument is under 0")
        return None
    elif n > 20:
        print("Argument is orver 20")
        return None
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test.py <number>")
    else:
        try:
            number = int(sys.argv[1])
            print(factorial(number))
        except ValueError:
            print("Invelid input. Please provide an integer.")