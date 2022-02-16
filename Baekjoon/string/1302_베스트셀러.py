n = int(input())
dic = {}

for _ in range(n):
    cur = input()
    if cur in dic:
        dic[cur] += 1
    else:
        dic[cur] = 1

print(sorted(dic.items(), key=lambda x: (-x[1], x[0]))[0][0])