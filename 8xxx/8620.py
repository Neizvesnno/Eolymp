n = int(input())
od = n%10
des = n//10%10
sot = n//100%10
tys = n//1000
if tys == sot == des and tys != od or tys == des == od and tys != sot or tys == sot == od and tys != des or sot == des == od and tys != sot:
    print("YES")
else:
    print("NO")
  
