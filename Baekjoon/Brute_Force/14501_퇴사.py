n = int(input())
max_res = 0
li = []

for _ in range(n):
    li.append(list(map(int, input().split())))

def recur(idx, s):
    global max_res
    if idx == n:
        max_res = max(max_res, s)
        return
    if idx > n:
        return
    recur(idx + li[idx][0], s + li[idx][1])
    recur(idx + 1, s)

recur(0, 0)
print(max_res)