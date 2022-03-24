n = int(input())
exp = input()
num, ope = [], []
res = -2 ** 31

start = 0
for i, e in enumerate(exp):
    if e in ['+', '-', '*']:
        num.append(exp[start:i])
        ope.append(exp[i])
        start = i + 1
    if i == len(exp) - 1:
        num.append(exp[start:])

def bf(num, ope, check):
    global res
    s = num[0]
    for i in range(len(ope)):
        s = str(eval(s + ope[i] + num[i + 1]))
    res = max(res, int(s))
    for i in range(len(ope)):
        if check[i] == 0 and check[i + 1] == 0:
            temp_num = num[0:i] + [str(eval(num[i] + ope[i] + num[i + 1]))] + num[i + 2:]
            temp_ope = ope[0:i] + ope[i + 1:]
            temp_check = check[0:i] + [1] + check[i + 2:]
            bf(temp_num, temp_ope, temp_check)

bf(num, ope, [0] * len(num))
print(res)