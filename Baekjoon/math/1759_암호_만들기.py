l, c = map(int, input().split())
li = sorted(list(input().split()))

def check(r):
    count = len(list(filter(lambda x: x in ['a', 'e', 'i', 'o', 'u'], r)))
    if count >= 1 and len(r) - count >= 2:
        return True
    return False

def find(r, idx):
    if len(r) == l and check(r):
        print(''.join(r))
        return
    for i in range(idx + 1, c):
        temp = r[:]
        temp.append(li[i])
        find(temp, i)

find([], -1)