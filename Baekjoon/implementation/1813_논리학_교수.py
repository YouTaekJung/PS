n = int(input())
li = [0] * 51
flag = []
num = list(map(int, input().split()))
for i in range(n):
    li[num[i]] += 1
for j in range(len(li)):
    if j == li[j]:
        flag.append(j)
print(-1 if flag == [] else max(flag))