n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
li = list(map(int, input().split()))

def search(t):
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if a[mid] == t:
            return True

        if t < a[mid]:
            right = mid - 1
        elif t > a[mid]:
            left = mid + 1

for i in range(m):
    print(1 if search(li[i]) else 0)