n = int(input())

count = 0

od = n % 10
des = n // 10 % 10
sot = n // 100 % 10
tys = n // 1000 % 10
dtys = n // 10000 % 10

if od % 2 != 0:
    count += 1
if des % 2 != 0:
    count += 1
if sot % 2 != 0:
    count += 1
if tys % 2 != 0:
    count += 1
if dtys % 2 != 0:
    count += 1

print(count)
