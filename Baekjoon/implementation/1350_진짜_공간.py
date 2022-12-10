n = int(input())
li = list(map(int, input().split()))
m = int(input())
ans = 0
for l in li:
    ans += l // m + 1 if l % m else l // m
print(ans * m)