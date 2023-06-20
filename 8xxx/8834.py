from math import*
x,y = map(float,input().split())
vid = 2 * x * y / sqrt(x * x + y * y) - (x + y - 1) * (x + y - 1) / (x * y)
print('%.3f'%vid)
