a, b = map(int, input().split())

def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

for i in range(a, b + 1):
    if i in [5, 7, 11]:
        print(i)
    elif len(str(i)) % 2 and str(i) == str(i)[::-1]:
        if is_prime(i):
            print(i)
print(-1)