s = input()
pw = input()
ans = len(s) ** (len(pw) - 1)

for i in range(len(pw)):
    ans += (s.index(pw[i])) * (len(s) ** (len(pw) - i - 1))
if len(s) == 1:
    print(len(pw))
else:
    print((ans + 1) % 900528)