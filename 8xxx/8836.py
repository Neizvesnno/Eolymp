import math
x, y = map(float,input().split())
kor = x**2+y**2-1
korn1 = math.sqrt(kor)
vid = ((2*x**3*y-4*x**2*y**2+2*x*y**3+x**2+y**2-1)/(2*x*y*korn1))
print('%.3f'%vid)
