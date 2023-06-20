n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i%2 != 0):
            print("*", end="")
        elif (i%4 == 2 and j == n): 
            print("*", end="")
        elif (i%4 == 0 and j == 1): 
            print("*", end="")
        else:
            print(" ", end="")
    print()
  
