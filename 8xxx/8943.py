n = int(input())

if n > 1:
    print("*" * 3)
    for i in range(n - 2):
        print("*", " ", "*", sep="")
    print("*" * 3)
elif n == 1:
    print("*" * 3)
  
