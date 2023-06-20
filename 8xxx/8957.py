n = int(input())
arr = list(map(int, input().split()))[:n:]

arr_res = []
zap_ch = 0

while True:
    zap_ch = arr[-1]

    if zap_ch % 2 == 0:
        arr_res.append(zap_ch)

    arr = arr[:-1:]

    if not arr:
        break

if len(arr_res) > 0:
    print(len(arr_res))

    for i in arr_res:
        print(i, end=" ")
else:
    print("NO")
  
