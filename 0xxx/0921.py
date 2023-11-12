n = int(input())
arr = list(map(float, input().split()))[:n:]

kol = 0
count = 0

for i in arr:
    if i < 0:
        count += i
        kol += 1

print(kol, "{0:.2f}".format(count))
