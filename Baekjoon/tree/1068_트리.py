n = int(input())
li = list(map(int, input().split()))
tree = [[] for _ in range(n)]
root = 0
rm = int(input())
count = 0

for i in range(len(li)):
    if li[i] == -1:
        root = i
    elif i == rm:
        continue
    else:
        tree[li[i]].append(i)

def dfs(node):
    global count
    if tree[node] == []:
        count += 1
    for t in tree[node]:
        dfs(t)

if rm == root:
    print(0)
else:
    dfs(root)
    print(count)