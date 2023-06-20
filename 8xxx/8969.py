n = int(input())
arr = list(map(int, input().split()))[:n:]

arr2 = [arr[0]]
suma = 0
kk = 1

for i in arr[1::]:
    for j in arr2:
        suma += j
    arr2.append(i - suma)
    kk += 1
    suma = 0

for res in arr2:
    print(res, end=" ")
  
