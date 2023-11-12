n = int(input())

arr = list(map(int, input().split()))[:n:]
new_arr = []

for i in reversed(range(0, len(arr))):
    if i != 0:
        if arr[i] > arr[i-1]:
            new_arr.append(arr[i])
            
for i in reversed(new_arr):
    print(i, end=" ")
  
