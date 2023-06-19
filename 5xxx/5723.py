n = int(input())
arr = list(map(int, input().split()))

booleta = False
arr.sort()
arr2 = [arr[0]]
arr = arr[1::]
kk = 1

if kk != n:
    while True:
        new_zap = arr[0]

        for i in arr2:
            if new_zap == i:
                booleta = True
                break

        if not booleta:
            arr2.append(new_zap)

        booleta = False
        arr = arr[1::]
        kk += 1

        if not arr or kk == n:
            break

lener = len(arr2)

if lener == 1:
    print(int(0))
else:
    print(lener)
  
