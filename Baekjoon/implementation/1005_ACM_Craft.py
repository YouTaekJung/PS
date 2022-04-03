t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))
    li = [[] for _ in range(n)]
    for _ in range(k):
        s, n = map(int, input().split())
        li[s - 1].append(n)
    print(li)