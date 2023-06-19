n = int(input())
arr = list(map(int, input().split()))

arr.sort()
arr_zap = arr
arr2 = [arr.count(arr[0])]
arr3 = [arr[0]]
arr = arr[1::]
zp_ch = 0
kk = 1

if kk != n:
    while True:
        new_zap = arr[0]
        
        for i in arr:
            if new_zap == i:
                zp_ch += 1
            else:
                break
        
        arr3.append(new_zap)
    
        
        arr2.append(zp_ch)
        arr = arr[zp_ch::]
        zp_ch = 0
        kk += 1
        
        if not arr or kk == n:
            break
        
zap_raz_arr = arr3
arr4 = []
kkh = 0
maximal = max(arr2)
arr_kkk = arr2

while True:
    if arr2[kkh] == maximal:
        arr4.append(arr3[kkh])
        
    kkh += 1
    arr_kkk = arr_kkk[1::]
    
    if not arr_kkk:
        break

len_arr = len(zap_raz_arr)
suma = sum(zap_raz_arr)
sr = suma / len_arr

closest = min(arr4, key = lambda x: abs(x - sr))
print(closest)
