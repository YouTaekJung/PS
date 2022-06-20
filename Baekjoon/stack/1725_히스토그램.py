import sys
input = sys.stdin.readline

n = int(input())
graph = [int(input()) for _ in range(n)] + [0]
left, ans = 0, 0
stack = [(0, graph[0])]
for right in range(1, n + 1):
    left = right
    while stack and stack[-1][1] > graph[right]:
        left, height = stack.pop()
        ans = max(ans, height * (right - left))
    stack.append((left, graph[right]))

print(ans)