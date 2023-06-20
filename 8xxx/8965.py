n = int(input())
arr = list(map(int, input().split()))[:n:]

arr_min = int(min(arr) / 2)
arr_res = []
zap_ch = 0

while True:
    zap_ch = arr[0]

    arr_res.append((zap_ch - arr_min))

    arr = arr[1::]

    if not arr:
        break

for i in arr_res:
    print(i, end=" ")
  
