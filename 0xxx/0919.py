n = int(input())
arr = list(map(float, input().split()))

index = 1
count = 0
suma = 0

for i in arr:

    if index % 3 == 0:
        if i > 0:
            count += 1
            suma += i
    index += 1

print(count, '{:.2f}'.format(suma))
