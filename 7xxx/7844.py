n = int(input())

arr = list(map(int, input().split()))[:n:]

for i in range(0, len(arr)):
    if i != len(arr)-1:
        if (arr[i] > 0 and arr[i+1] > 0) or (arr[i] < 0 and arr[i+1] < 0):
            print(arr[i], arr[i+1])
          
