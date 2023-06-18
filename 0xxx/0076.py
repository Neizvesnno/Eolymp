a, b, x, y, z = map(int,input().split())
if 0 < a < 10 and 0 < b < 10 and 0 < x < 10 and 0 < y < 10 and 0 < z < 10:
    if a > x and b > y:
        print(1)
    elif a > x and b > z:
        print(1)
    elif a > y and b > z:
        print(1)
    elif b > x and a > y:
        print(1)
    elif b > x and a > z:
        print(1)
    elif b > y and a > z:
        print(1)
    else:
        print(0)
      
