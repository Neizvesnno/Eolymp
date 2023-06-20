n, m = map(int, input().split())

if n != 1:
    
    print("*" * m)

    if m != 1:
        for i in range(0, n - 2):
            print("*", end="")
            for j in range(m - 2):
                print(" ", end="")
            print("*")
    else:
        for i in range(n - 2):
            print("*")

    print("*" * m)
else:
    print("*" * m)
  
