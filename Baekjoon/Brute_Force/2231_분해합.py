n = int(input())
i = 1
while i < n:
    if i + sum(list(map(int, list(str(i))))) == n:
        print(i)
        break
    i += 1

if i == n:
    print(0)