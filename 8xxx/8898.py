import math
n = int(input())
n = n + 1 
while True:
    res = math.floor(math.sqrt(n))
    if res**2 == n:
        print(n)
        break
    n = n + 1
  
