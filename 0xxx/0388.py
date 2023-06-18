n = int(input())

k = 0

if n == 1:
    print(k)
else:
    while n > 0:
        if n % 2 == 0:
            n = n//2
            k  += 1
        elif n % 2 != 0:
            n += 1
            k += 1
        if n == 1:
            print(k)
            break
