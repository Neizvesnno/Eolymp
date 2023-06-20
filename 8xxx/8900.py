n = int(input())
if n % 7 == 0:
    n += 7
else:
    while True:
        if n % 7 != 0:
            n += 1
        else:
            break

print(n)
