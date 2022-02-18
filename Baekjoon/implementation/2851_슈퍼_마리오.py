li = []
acc = []
while True:
    try:
        li.insert(0, int(input()))
        acc.insert(0, abs(-100 + sum(li)))
    except:
        break

print(sum(li[acc.index(min(acc)):]))