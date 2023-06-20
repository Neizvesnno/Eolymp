n = int(input())
arr = list(map(int, input().split()))[:n:]

arr_res = []
arr_min = min(arr)
arr_max = max(arr)

while True:

    if arr[0] != arr_max and arr[0] != arr_min:
        arr_res.append(arr[0])

    arr = arr[1::]

    if not arr:
        print(sum(arr_res))
        break
      
