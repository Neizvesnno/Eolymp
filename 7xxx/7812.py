a,b,c,d = map(int,input().split())

if a >= c and a >= b and a >= d:
    print(a)
elif b >= c and b >= a and b >= d:
    print(b)
elif c >= a and c >= d and c >= b:
    print(c)
else:
    print(d)
  
