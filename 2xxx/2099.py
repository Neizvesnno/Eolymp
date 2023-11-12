n = int(input())
arr1 = list(map(int, input().split()))[:n:]
n = int(input())
arr2 = list(map(int, input().split()))[:n:]

arr_res = []

counter = 0

for i in arr1:
    if i not in arr2:
        counter += 1
        arr_res.append(i)

print(counter)

for i in arr_res:
    print(i, end=" ")
  
