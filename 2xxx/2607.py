n = int(input())

i = 1
k1 = 0
k2 = 0

while n>0:
	if i%2 != 0:
		k1 = k1 + n%10
	else:
		k2 = k2 + n%10
		
	n = n//10
	i = i + 1

print(k1*k2)
