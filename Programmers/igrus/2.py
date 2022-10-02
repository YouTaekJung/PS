n, p = int(input()), int(input())
price = [p - 500, 0.9 * p, p - 2000, 0.75 * p]
print(int(max(0, min([p, *price[:n//5]]))))