word = input()
l = len(word)

dic = {}
for i in range(l):
    if word[i] in dic:
        dic[word[i]] += 1
    else:
        dic[word[i]] = 1

if l % 2:
    if list(map(lambda x: x[1] % 2, dic.items())).count(1) != 1:
        print('I\'m Sorry Hansoo')
    else:
        center = list(filter(lambda x: x[1] % 2, dic.items()))[0]
        dic[center[0]] -= 1
        res = ''
        items = sorted(dic.items())
        for item in items:
            res += item[0] * (item[1] // 2)
        print(res + center[0] + res[::-1])
else:
    if list(map(lambda x: x[1] % 2, dic.items())).count(1) >= 1:
        print('I\'m Sorry Hansoo')
    else:
        res = ''
        items = sorted(dic.items())
        for item in items:
            res += item[0] * (item[1] // 2)
        print(res + res[::-1])
