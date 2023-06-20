n = int(input())
arr = list(map(int, input().split()))[:n:]

arr_min = min(arr)
arr_zap = [0]
zap_ch = 0
zap_zx = arr[0]
kk = 0

for i in arr[1::]:
    arr_zap.append(i)

while True:
    zap_ch = arr[0]

    if zap_ch == arr_min:
        arr_zap[kk] = zap_zx
        arr_zap[0] = zap_ch
        break

    arr = arr[1::]
    kk += 1

for i in arr_zap:
    print(i, end=" ")
  
