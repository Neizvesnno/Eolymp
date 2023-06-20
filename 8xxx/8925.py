n = int(input())

booleta = False
res = 1

for i in str(n):
    if int(i) % 2 != 0:
        res *= int(i)
        booleta = True


if booleta:
    print(res)
else:
    print(-1)
  
