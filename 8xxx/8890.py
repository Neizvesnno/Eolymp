n = int(input())
od = n%10
des = n//10%10
sot = n//100%10
tys = n//1000%10
dest = n//10000%10
if od%2 == 0:
    od = (od+1)
if des%2 == 0:
    des = (des+1)
if sot%2 == 0:
    sot = (sot+1)
if tys%2 == 0:
    tys = (tys+1)
if dest%2 == 0:
    dest = (dest+1)
print(dest*10000+tys*1000+sot*100+des*10+od)
