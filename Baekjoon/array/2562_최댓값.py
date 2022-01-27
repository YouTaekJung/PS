m = 0
c = 1
while True:
    try:
        n = int(input())
        if m < n:
            m = n
            i = c
        c += 1
    except:
        break
print(m)
print(i)