n = int(input())
od = n%10
des = n//10%10
sot = n//100%10
tys = n//1000
if tys == sot and des == od and tys != des or tys == des and sot == od and tys != sot or tys == od and sot == des and tys != sot:
    print("YES")
else:
    print("NO")
  
