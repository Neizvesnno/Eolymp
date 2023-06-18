import math
A,B,Z = map(int,input().split())
vid = Z*math.pi/180
res = math.sin(vid)/math.cos(vid)
if Z == 90:
    S = A*B*math.sqrt(2)
elif 2*B < A*res:
    S = (A*A/2-(A-B*math.sqrt(2)/res)**2/2)/math.cos(vid)
else:
    S = A*A/2/math.cos(vid)
print("%.3f"%S)
