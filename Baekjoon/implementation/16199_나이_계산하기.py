y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
age = y2 - y1

if (m1 == m2 and d1 > d2) or m1 > m2:
    age -= 1

print(age)
print(y2 - y1 + 1)
print(y2 - y1)