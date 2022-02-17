n, m1 = map(int, input().split())
matrix1 = []
for _ in range(n):
    matrix1.append(list(map(int, input().split())))

m2, k = map(int, input().split())
matrix2 = []
for _ in range(m2):
    matrix2.append(list(map(int, input().split())))

result = [[0 for _ in range(k)] for _ in range(n)]
for x in range(n):
    for y in range(k):
        for m in range(m1):
            result[x][y] += matrix1[x][m] * matrix2[m][y]

for row in result:
    for num in row:
        print(num, end=' ')
    print()