n = int(input())

arr = list(map(int, input().split()))

count = 1
res_count = count
maximum = arr[0]

for i in arr:
    if i > maximum:
        res_count = count 
        maximum = i
    count += 1

print(maximum, res_count)
