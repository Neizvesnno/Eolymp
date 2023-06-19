a,b,c = map(int,input().split())

d = (a+b+c)//2

if (a+b+c)//2 == (a+b+c)/2:
    if a+b == d or b+c == d or a+c == d:
        print(0)
    else:
        if a>d:
            print(1)
            print(d-b, d-c)
        elif a+b > d:
            print(2)
            print(d-a, d-c)
        else:
            print(3)
            print(d-a, d-b)
else:
    print(-1)
  
