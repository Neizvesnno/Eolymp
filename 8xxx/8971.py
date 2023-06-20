n = int(input())
arr = list(map(int, input().split()))[:n:]

kk = 1
arr2 = []

while True:
    zap_ch = arr[0]

    for i in arr[1::]:
        if i == zap_ch:
            arr.pop(kk)
        else:
            kk += 1

    arr2.append(arr[0])
    arr = arr[1::]
    kk = 1

    if not arr:
        break

for j in arr2:
    print(j, end=" ")
  
