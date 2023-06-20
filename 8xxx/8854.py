n=int(input())
od=n%10
des=n//10%10
sot=n//100%10
tys=n//1000%10
dest=n//10000
vid=(od*10000+des*1000+sot*100+tys*10+dest)
print(vid)
