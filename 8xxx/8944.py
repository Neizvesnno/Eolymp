n = int(input())

if n > 1:
    print("*" * n)

    for i in range(0, n - 2):
        print("*", end="")
        for j in range(n - 2):
            print(" ", end="")
        print("*")

    print("*" * n)
else:
    print("*")
  
