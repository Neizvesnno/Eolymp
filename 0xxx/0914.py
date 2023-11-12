n = int(input())
arr = list(map(float, input().split()))[:n:]

arr_new = []

for i in arr:
    arr_new.append((abs(i)))

print("{0:.2f}".format(max(arr_new)))
