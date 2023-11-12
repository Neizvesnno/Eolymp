n = int(input())

arr = list(map(int, input().split()))[:n:]
count = 0

while True:
    print(arr[count+1], arr[count], end=" ")

    count += 2

    if count >= len(arr)-1:
        break

if count < len(arr):
    print(arr[-1])
  
