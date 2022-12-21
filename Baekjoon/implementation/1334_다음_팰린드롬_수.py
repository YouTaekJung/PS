n = int(input()) + 1

def is_palindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    return False

while True:
    if is_palindrome(n):
        print(n)
        exit()
    n += 1