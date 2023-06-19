n = int(input())
arr = list(map(int, input().split()))

k = 0
max_kol= 0
max_zp = 0

while True:
    for i in arr:
        if i == arr[k]:
            max_zp += 1
            
    if max_zp > max_kol:
        max_kol = max_zp
        
    k += 1
    max_zp = 0
    
    if k == len(arr):
        break
    
arr2 = list()
zp2 = 0
vc = 0
c = 0

while True:
    vc = arr[c]
    
    for i in arr:
        if arr[c] == i:
            zp2 += 1
            
    if zp2 == max_kol:
        arr2.append(vc)
        
    c += 1
    
    if c == len(arr):
        break
    
    zp2 = 0


print(min(arr2))
