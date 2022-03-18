n = int(input())
li = list(map(int, input().split()))

p_two = []
p_three = []
for i in [0, 5]:
    for j in [1, 4]:
        for k in [2, 3]:
            p_two.append(min([li[i] + li[j], li[i] + li[k], li[k] + li[j]]))
            p_three.append(li[i] + li[j] + li[k])

one, two, three = min(li), min(p_two), min(p_three)

if n == 1:
    print(sum(li) - max(li))
else:
    print(one * (n - 2) * (5 * n - 6) + 4 * (two * (2 * n - 3) + three))