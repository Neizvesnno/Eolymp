m = int(input())
ch = 1
kr = 1
while True:
	kr = ch ** 2
	if kr <= m:
		ch = ch + 1
		print(kr, end=" ")
	else:
		break
    
