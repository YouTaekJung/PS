n = int(input())
count = 0
li = [0] * n

def recur(x, li):
	check = [0] * n
	if x == n:
		global count
		count += 1
		return

	for i in range(x):
		check[li[i]] = 1
		if 0 <= li[i] + (x - i) < n:
			check[li[i] + (x - i)] = 1
		if 0 <= li[i] - (x - i) < n:
			check[li[i] - (x - i)] = 1

	for i in range(n):
		if check[i] == 0:
			li[x] = i
			recur(x + 1, li)
	return

recur(0, li)
print(count)