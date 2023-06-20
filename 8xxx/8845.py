n=int(input())
od=n%10
des=n//10%10
sot=n//100%10
tys=n//1000
vid=(tys*100+des*10+od)
print(vid)
