import sys

n = int(input())
arr = list(map(float, input().split()))[:n:]

arr_new = []

for i in arr:
    if i > 0:
        arr_new.append(i)

if len(arr_new) == 0:
    print('Not Found')
    sys.exit(0)

res = 0
kol = len(arr_new)

for i in arr_new:
    res += i

print("{0:.2f}".format(float(res/kol)))
