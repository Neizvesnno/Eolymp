n = int(input())
od = n%10
des = n//10%10
sot = n//100%10
tys = n//1000
if tys%2 == 1 or sot%2 == 1 or des%2 == 1 or od%2 == 1:
    print("YES")
else:
    print("NO")
  
