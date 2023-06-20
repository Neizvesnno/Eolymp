n = int(input())
arr = list(map(int, input().split()))[:n:]

arr_min = min(arr)
arr2 = []
arr3 = []
zap_ch = 0
kol = 0

while True:
    zap_ch = arr[0]

    if zap_ch != arr_min:
        arr2.append(zap_ch)
    else:
        kol += 1

    arr = arr[1::]

    if not arr:
        break

for i in range(0, kol):
    arr3.append(arr_min)

for j in arr2:
    arr3.append(j)

for res in arr3:
    print(res, end=" ")
  
