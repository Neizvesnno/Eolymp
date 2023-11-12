n = int(input())
arr = list(map(int, input().split()))[:n:]

if len(arr) > 1:
    print(arr[-1], end=" ")
    for i in arr[:len(arr)-1:]:
        print(i, end=" ")
else:
    print(arr[0])
  
