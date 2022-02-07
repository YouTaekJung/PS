import collections
n, m, v = map(int, input().split())

matrix = [[0] * (n+1) for i in range(n+1)]
check = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(v):
    check[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if matrix[v][i] == 1 and check[i] == 0:
            dfs(i)

def bfs(v):
    queue = collections.deque()
    queue.append(v)
    check[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if matrix[v][i] == 1 and check[i] == 0:
                queue.append(i)
                check[i] = 1

dfs(v)
check = [0] * (n+1)
print()
bfs(v)