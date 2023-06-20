n=int(input())
od=n%10
des=n//10%10
sot=n//100%10
tys=n//1000
vid=(od*1000+des*100+sot*10+tys)
print(vid)
