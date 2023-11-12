import sys

n = int(input())

arr = list(map(int, input().split()))[:n:]

counter = 0
lenner = len(arr)

for i in arr:
    counter += i

counter_res = 0

if int(counter/lenner) == counter/lenner:
    prb = counter/lenner
    arr_nedo = []

    for i in arr:
        if i < prb:
            arr_nedo.append(i)

    arr_nedo.sort()
    arr_nedo = arr_nedo[::-1]

    while True:
        zap_ch = arr_nedo[0]

        while True:
            if zap_ch < prb:
                counter_res += 1
                zap_ch += 1
            else:
                break

        arr_nedo = arr_nedo[1::]

        if not arr_nedo:
            break

    print(counter_res)
else:
    print(-1)
  
