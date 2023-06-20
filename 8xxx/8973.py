n = int(input())
arr = list(map(int, input().split()))[:n:]

arr2 = []
kk = len(arr) - 2
zap_ch = 0

while True:
    zap_ch = arr[-1]

    for i in reversed(arr[:-1:]):
        if i == zap_ch:
            arr.pop(kk)
        kk -= 1

    arr2.append(arr[kk])
    arr = arr[:-1:]
    kk = len(arr) - 2

    if not arr:
        break

for j in reversed(arr2):
    print(j, end=" ")
  
