n = int(input())
arr = list(map(int, input().split()))[:n:]

arr2 = []
kk = len(arr) - 2
zap_ch = 0
booleta = False

while True:
    zap_ch = arr[-1]

    for i in reversed(arr[:-1:]):
        if i == zap_ch:
            arr.pop(kk)
            booleta = True
        kk -= 1

    if booleta:
        arr2.append(arr[kk])

    booleta = False
    arr = arr[:-1:]
    kk = len(arr) - 2

    if not arr:
        break

if not arr2:
    print("NO")
else:
    for j in reversed(arr2):
        print(j, end=" ")
      
