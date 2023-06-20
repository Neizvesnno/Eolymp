vid = []
count = 0
res = True
while res:
	n = int(input())
	if n == 0:
		res = False
	else:
		vid.append(n)
for i in vid:
	if i%2 == 0:
		count += i
print(count)
