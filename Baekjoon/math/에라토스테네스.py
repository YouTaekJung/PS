def prime(n):
    li = [0, 0] + [1] * n

    for i in range(2, n + 1):
        if li[i]:
            for j in range(2 * i, n + 1, i):
                li[j] = 0

    return [i for i in range(n) if li[i] == 1]

print(prime(10))