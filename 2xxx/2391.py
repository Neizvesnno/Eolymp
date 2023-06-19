from math import*

a,b,n = map(int,input().split())
vid = n/60
v = ceil(vid)
c = v*b
if n == 0:
    print(0)
else:
    print(c+a)
  
