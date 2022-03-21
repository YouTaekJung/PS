n, m = map(int, input().split())
count = 0
temp = []
temp_count = 0

def dfs():
    global count, temp_count
    if temp_count == n:
        count += 1
        if count == m:
            print('+'.join(list(map(str, temp))))
        return

    for i in range(1, 4):
        if temp_count + i <= n:
            temp.append(i)
            temp_count += i
            dfs()
            temp.pop()
            temp_count -= i

dfs()
if count < m:
    print(-1)