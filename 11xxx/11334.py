n = int(input())
arr = [int(i) for i in input().split()]
dodch = 0
vidch = 0
null = 0

for i in range(n):
    if arr[i] > 0:
        dodch += 1
    elif arr[i] < 0:
        vidch += 1
    else:
        null += 1

print(dodch, vidch, null)
