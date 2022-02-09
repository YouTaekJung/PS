n = int(input())
li = []

for _ in range(n):
    li.append(int(input()))

dic = {}
for num in li:
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 0
dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

end = 0
max = dic[0][1]
for i in range(1, len(dic)):
    if max == dic[i][1]:
        end += 1
    else:
        break

li = sorted(li)

print(round(sum(li) / n))
print(li[int(n // 2)] if n % 2 else (li[int(n // 2)] + li[int(n // 2) - 1]) / 2)
if n == 1:
    print(li[0])
elif dic[0][1] == 0:
    print(li[1])
else:
    print(dic[end-1][0] if end else dic[0][0])
print(li[-1] - li[0])