from math import factorial

n = int(input())
board = [list(map(int, input().split())) for _ in range(5)]

print(factorial(2 * n) // (factorial(n) ** 2) % 1000000007, n ** 2)