n = int(input())
if n % 11 == 0:
    n -= 11
else:
    while True:
        if n % 11 != 0:
            n -= 1
        else:
            break

print(n)
