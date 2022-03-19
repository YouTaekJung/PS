w = input()
count = 0
res = 0
i = 0
while i < len(w):
    if i != len(w) - 1 and w[i] == '(' and w[i + 1] == ')':
        res += count
        i += 1
    elif w[i] == '(':
        count += 1
    else:
        count -= 1
        res += 1
    i += 1

print(res)