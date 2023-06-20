a, b = map(int, input().split())

for res in range(a, b + 1):

    tys = res // 1000 % 10
    sot = res // 100 % 10
    des = res // 10 % 10
    od = res % 10

    if tys ** 4 + sot ** 4 + des ** 4 + od ** 4 == res:
        print(tys * 1000 + sot * 100 + des * 10 + od, end=" ")
    
