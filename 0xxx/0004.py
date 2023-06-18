import math

x1, y1, r1, x2, y2, r2 = map(float,input().split())

res = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if res == 0:
    print(-1)
elif res == (r1 + r2) or res == (r1 - r2):
    print(1)
elif (r1 - r2) < res < (r1 + r2):
    print(2)
else:
    print(0)
  
