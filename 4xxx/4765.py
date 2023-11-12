n = int(input())
arr = list(map(int, input().split()))

arr_res = [arr[0]]
arr_zap = arr
counter = 0

while True:
    arr = arr[1::]

    if not arr:
        break
 
    zap_ch = arr[0]

    if zap_ch != arr_zap[counter]:
        arr_res.append(zap_ch)

    counter += 1

for i in arr_res:
    print(i, end=" ")
  
