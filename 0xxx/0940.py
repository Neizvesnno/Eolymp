import math

n = int(input())
arr = list(map(int, input().split()))[:n:]

if n % 2 == 0:
    maj = math.ceil(n/2) + 1
else:
    maj = math.ceil(n/2)

count = 0

while True:
    zap_ch = arr[0]
    zap_arr = arr
    arrka = []

    while True:
        if zap_arr[0] == zap_ch:
            count += 1
        else:
            arrka.append(zap_arr[0])
        zap_arr = zap_arr[1::]

        if not zap_arr:
            break
    if count >= maj:
        print(zap_ch)
        break
    else:
        arr = arrka
        count = 0

    if len(arr) == 0:
        print(-1)
        break
      
