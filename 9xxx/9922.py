n = int(input())
c = str(input())

while True:
    if n != 1:
        n -= 1
        print(c + "+", end="")
    else:
        print(c)
        break
      
