n = int(input())

if n%10 == 0:
    print(n + 10)
else:
    while True:
        if n % 10 != 0:
            n = n + 1
        else:
            print(n)
            break
          
