n = int(input())
arr = list(map(int, input().split()))[:n:]

arr2 = []
kk = 0
par = len(arr)
pod = 0

if par % 2 != 0:
    par = (par + 1) / 2
else:
    par = par / 2

for i in range(len(arr)):
    arr2.append(0)

while True:

    if kk % 2 == 0:
        arr2[kk] = arr[pod]
        pod += 1
    else:
        arr2[kk] = arr[int(par)]
        par += 1

    kk += 1
    n -= 1

    if not n:
        break

for i in arr2:
    print(i, end=" ")
  
