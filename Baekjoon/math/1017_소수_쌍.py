prime = [1] * 2000

for i in range(2, 2000):
    if prime[i]:
        for j in range(2 * i, 2000, i):
            prime[j] = 0

n = int(input())
li = list(map(int, input().split()))
odd, even = [], []
ans = []
for l in li:
    if l % 2:
        odd.append(l)
    else:
        even.append(l)

check = [[0] * (n // 2), [0] * (n // 2)]
check[0][0] = 1
temp = []

def dfs():
    if sum(sum(check, [])) == n:
        ans.append(temp[1])
    for i in

for i in range(n // 2):
    if prime[odd[0] + even[i]]:
        temp.append([0, i])
        check[1][i] = 1
        dfs()
