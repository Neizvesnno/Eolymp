n = int(input())
arr = list(map(float, input().split()))

Result = None
count = 0

for i in range(0, n):
    count += 1
    if arr[i] <= 2.5:
        Result = arr[i]
        break

if Result is None:
    print("Not Found")
else:
    can = "{0:.2f}".format(float(Result))
    print(count, can)
  
