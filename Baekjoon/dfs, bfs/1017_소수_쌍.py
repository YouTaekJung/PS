def get_prime(n):
    li = [0, 0] + [1] * n
    for i in range(2, n + 1):
        if li[i]:
            for j in range(2 * i, n + 1, i):
                li[j] = 0
    return li

def bimatch(num):
    if visited[num]:
        return False
    visited[num] = 1
    for g in graph[num]:
        if selected[g] == -1 or bimatch(selected[g]):
            selected[g] = num
            visited[g] = 1
            return True
    return False

n = int(input())
li = list(map(int, input().split()))
prime = get_prime(2000)
odd, even = [], []
for i in range(n):
    if li[i] % 2:
        odd.append(li[i])
    else:
        even.append(li[i])

if len(even) != n // 2:
    print(-1)
    exit()

first = odd if li[0] % 2 else even
rem = even if li[0] % 2 else odd
graph = [[] for _ in range(len(first))]
for i, f in enumerate(first):
    for j, r in enumerate(rem):
        if prime[f + r]:
            graph[i].append(j)

ans = []
for i in graph[0]:
    selected = [-1] * len(rem)
    selected[i] = 0
    count = 1
    for j in range(1, len(first)):
        visited = [0] * len(first)
        visited[0] = 1
        count += bimatch(j)
    if count == n // 2:
        ans.append(rem[i])
if ans == []:
    print(-1)
else:
    print(*sorted(ans))