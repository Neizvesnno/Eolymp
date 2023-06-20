n = int(input())
od = n%10
des = n//10%10
sot = n//100%10
tys = n//1000
print(tys*1000+sot*100+od*10+des)
