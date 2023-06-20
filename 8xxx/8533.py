a,b = map(int,input().split())
for i in range(a, b + 1):
    od = i%10
    des = i//10%10
    sot = i//100%10
    tys = i//1000
    if od != des and od != sot and od != tys and des != od and des != sot and des != tys and sot != od and sot != des and sot != tys and tys != od and tys != des and tys != sot:
        print(i, end=" ")
      
