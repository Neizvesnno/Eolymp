n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = list(map(list, zip(*a)))[::-1]
sn = []
sm = []
for i in range(n):
    sn.append(sum(a[i]))
for i in range(m):
    sm.append(sum(b[i]))
sn.sort()
sm.sort()
if sn[0] == sm[0] and sn[1] == sn[-1] and sm[1] == sm[-1] and sm[-1] == sm[-1]:
    print("Yes")
elif sn[n-1] == sm[-1] and sn[0] == sm[-2] and sm[0] == sm[-2] and sn[0] == sm[0]:
    print("Yes")
else:
    print("No")
    
