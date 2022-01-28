[a, b, c] = [int(input()) for _ in range(3)]

result = list(str(a * b * c))
for i in range(10):
    print(result.count(str(i)))