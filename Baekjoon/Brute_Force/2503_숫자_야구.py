from itertools import permutations

n = int(input())
per = list(permutations(range(1, 10), 3))

for _ in range(n):
    num, s, b = map(int, input().split())
    num = list(str(num))
    count = 0
    for i in range(len(per)):
        s_cnt = b_cnt = 0
        i -= count

        for j in range(3):
            num[j] = int(num[j])
            if num[j] in per[i]:
                if j == per[i].index(num[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1
        if s_cnt != s or b_cnt != b:
            per.remove(per[i])
            count += 1
print(len(per))