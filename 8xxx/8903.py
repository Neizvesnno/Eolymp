n = int(input())
if n % 5 == 0:
    n -= 5
else:
    while True:
        if n % 5 != 0:
            n -= 1
        else:
            break

print(n)
