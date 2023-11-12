n = int(input())

if n == 1:
    print(1)
    exit(0)

arr = sum(list(map(int, input().split())))
sumarka = 0

for i in range(0, n+1):
    sumarka += i

print(sumarka - arr)
