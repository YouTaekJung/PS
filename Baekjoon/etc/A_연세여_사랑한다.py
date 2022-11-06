cur = input()
password = "ILOVEYONSEI"

ans = 0
for p in password:
    ans += abs(ord(p) - ord(cur))
    cur = p
print(ans)