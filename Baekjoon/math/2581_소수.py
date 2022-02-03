m = int(input())
n = int(input())
li = []
for num in range(m, n + 1):
    if num == 2:
        li.append(num)
    for i in range(2, num):
        if num % i == 0:
            break
        if i == num - 1:
            li.append(num)
if len(li) == 0:
    print(-1)
else:
    print(sum(li))
    print(min(li))