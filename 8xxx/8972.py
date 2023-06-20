n = int(input())
arr = list(map(int, input().split()))[:n:]

arr2 = []
zap_ch = 0
booleta = False
kk = 1

while True:
    zap_ch = arr[0]

    for i in arr[1::]:
        if i == zap_ch:
            booleta = True
            arr.pop(kk)
        else:
            kk += 1

    if booleta:
        arr2.append(arr[0])

    booleta = False
    kk = 1
    arr = arr[1::]

    if not arr:
        break

if not arr2:
    print("NO")
else:
    for j in arr2:
        print(j, end=" ")
      
