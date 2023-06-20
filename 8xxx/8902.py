n = int(input())
w = 0
while True:
    n += 1
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
        break

print(n)
