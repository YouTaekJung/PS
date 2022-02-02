str = input().upper()
s = set(str)
d = {}
for i in s:
    d[i] = str.count(i)
res = sorted(d.items(), key=lambda x: x[1], reverse=True)

if len(res) == 1:
    print(res[0][0])
else:
    if res[0][1] == res[1][1]:
        print('?')
    else:
        print(res[0][0])