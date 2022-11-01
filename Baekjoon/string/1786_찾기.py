def get_pi(p):
    n, j = len(p), 0
    pi = [0] * n
    for i in range(1, n):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
        if p[i] == p[j]:
            pi[i] = j + 1
            j += 1
    return pi

def kmp(t, p):
    j, res = 0, []
    n, m = len(t), len(p)
    pi = get_pi(p)
    for i in range(n):
        while j > 0 and t[i] != p[j]:
            j = pi[j - 1]
        if t[i] == p[j]:
            if j == m - 1:
                res.append(i - m + 2)
                j = pi[j]
            else:
                j += 1
    return res

t, p = input(), input()
ans = kmp(t, p)
print(len(ans))
print(*ans)