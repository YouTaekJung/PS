n = int(input())
li = list(map(int, input().split()))
ans, stack = [-1] * n, []
count = {0: 0}

for l in li:
    if l in count:
        count[l] += 1
    else:
        count[l] = 1

stack.append(0)
for i in range(1, n):
    while stack and count[li[stack[-1]]] < count[li[i]]:
        ans[stack.pop()] = li[i]
    stack.append(i)

print(*ans)