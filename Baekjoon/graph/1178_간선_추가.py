v, e = map(int, input().split())
graph = [0] * v

for _ in range(e):
    x, y = map(lambda x: int(x) - 1, input().split())
    graph[x] += 1
    graph[y] += 1

odd = len(list(filter(lambda x: x % 2, graph)))
if odd in [0, 2]:
    print(0)
elif odd == 1:
    print(1)
else:
    print((odd - 2) // 2 + odd % 2)