n = int(input())
arr = list(map(int, input().split()))

minimal = arr[0]
maximum = 0

for i in range(0, n):
    if arr[i] > maximum:
        maximum = arr[i]
    if arr[i] < minimal:
        minimal = arr[i]

print(maximum - minimal)
