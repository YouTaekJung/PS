for _ in range(int(input())):
    input()
    n = int(input())
    li = [int(input()) for _ in range(n)]
    print("NO" if sum(li) % n else "YES")