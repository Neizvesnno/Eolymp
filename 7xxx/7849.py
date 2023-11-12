n = int(input())

arr = list(map(int, input().split()))[:n:]

min_arr = min(arr)
max_arr = max(arr)
arr_new = []

for i in range(0, len(arr)):
    if int(arr[i]) == min(arr):
        arr_new.append('m')
    elif int(arr[i]) == max(arr):
        arr_new.append('z')
    else:
        arr_new.append(arr[i])

for i in range(0, len(arr_new)):
    if str(arr_new[i]) == 'm':
        arr_new[i] = max_arr
    elif str(arr_new[i]) == 'z':
        arr_new[i] = min_arr

    print(arr_new[i], end=" ")
  
