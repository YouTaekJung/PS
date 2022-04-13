n, m = int(input()), int(input())
li = list(set(range(10)) - set(map(int, input().split())))
ans = abs(n - 100)

for num in range(1000001):
    num = str(num)
    for i in range(len(num)):
        if int(num[i]) not in li:
            break
        elif i == len(num) - 1:
            ans = min(ans, abs(n - int(num)) + len(str(num)))

print(ans)