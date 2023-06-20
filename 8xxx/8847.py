n=int(input())
od=n%10
des=n//10%10
sot=n//100%10
tys=n//1000
vid=(tys*1000+od*100+des*10+sot)
print(vid)
