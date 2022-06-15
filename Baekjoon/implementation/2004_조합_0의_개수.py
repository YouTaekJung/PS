n, m = map(int, input().split())

def count(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count

five = count(n, 5) - count(m, 5) - count(n - m, 5)
two = count(n, 2) - count(m, 2) - count(n - m, 2)
print(min(five, two))