res = []
n = int(input())
m = 0
for i in range(0, n):
	m += 2
	res.append(m)
print(*res, end=" ")
