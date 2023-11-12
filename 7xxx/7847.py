n = int(input())

arr = list(map(int, input().split()))[:n:]

arr_res = []
count = 0

for i in arr:
    if i not in arr_res:
        arr_res.append(i)
        count += 1

print(count)
