n = int(input())

count = 0

while True:
    if 2 ** count <= n:
        count = count + 1
    else:
        break

print(2 ** count)
