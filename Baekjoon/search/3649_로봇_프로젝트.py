import sys
input = sys.stdin.readline

while True:
    try:
        x, n = int(input().rstrip()) * 10000000, int(input().rstrip())
        li = sorted([int(input().rstrip()) for _ in range(n)])
        left, right, check = 0, n - 1, 1
        while left < right:
            s = li[left] + li[right]
            if s == x:
                print('yes', li[left], li[right])
                check = 0
                break
            elif s < x:
                left += 1
            else:
                right -= 1
        if check:
            print('danger')
    except:
        break
