t1, x1, s1 = map(int,input().split())
t2, x2, s2 = map(int,input().split())

if s2 < s1:
    x2 = x2 - 1
    s2 = s2 + 60
if x2 < x1:
    t2 = t2 - 1
    x2 = x2 + 60

a = t2 - t1
b = x2 - x1
c = s2 - s1

print(a, b, c)
