n = int(input())

od = n%10
des = n//10%10
sot = n//100%10

print(od*100+des*10+sot)
