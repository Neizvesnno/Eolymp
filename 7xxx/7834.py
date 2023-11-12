n = int(input())
arr = list(map(int, input().split()))

arr.sort()
arr = arr[::-1]

if len(arr) > 1:
    print(arr[0] + arr[1])
elif len(arr) == 1:
    print(arr[0])
else:
    print(0)
  
