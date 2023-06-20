count = 0
while True:
    n = int(input())
    if n%2 != 0:
        count = count + 1
    elif n == 0:
        break

print(count)
