n = int(input())
arr = list(map(int, input().split()))[:n:]

max_arr = max(arr)
arr_len = len(arr)
kk = len(arr) - 1
zap_zx = arr[-1]
arr_res = arr
zap_ch = 0

while True:
    zap_ch = arr[-1]

    if zap_ch == max_arr:
        arr_res[arr_len - 1] = zap_ch
        arr_res[kk] = zap_zx
        break

    kk -= 1
    arr = arr[:-1:]

for i in arr_res:
    print(i, end=" ")
  
