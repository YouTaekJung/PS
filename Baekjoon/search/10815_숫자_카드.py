n = int(input())
li = sorted(list(map(int, input().split())))
m = int(input())
s = list(map(int, input().split()))

def search(x, s, e):
    while s <= e:
        mid = (s + e) // 2
        if li[mid] == x:
            return 1
        elif li[mid] > x:
            e = mid - 1
        else:
            s = mid + 1
    return 0

print(*list(map(lambda x: search(x, 0, n - 1), s)))