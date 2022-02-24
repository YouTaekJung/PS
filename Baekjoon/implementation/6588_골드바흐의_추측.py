li = []
m = 0

while True:
    n = int(input())
    if n == 0:
        break
    m = max(m, n)
    li.append(n)

check = [True] * (m + 1)

for i in range(2, m + 1):
    for j in range(2 * i, m + 1, i):
        if check[j]:
            check[j] = False

for n in li:
    for i in range(2, n // 2 + 1):
        if check[i] and check[n - i]:
            print(f'{n} = {i} + {n - i}')
            break
        if i == n // 2:
            print("Goldbach\'s conjecture is wrong.")
