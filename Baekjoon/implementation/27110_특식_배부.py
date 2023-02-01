n = int(input())
li = list(map(int, input().split()))
print(sum(map(lambda x: min(n, x), li)))