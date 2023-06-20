n = int(input())
od = n%10
des = n//10%10
sot = n//100%10
tys = n//1000
if tys%2 == 0 and sot%2 == 0 and des%2 == 0 and od%2 == 0:
    print("YES")
else:
    print("NO")
  
