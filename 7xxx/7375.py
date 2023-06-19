M = int(input())

v5 = M//5
if M%5 == 0:
    print(v5)
elif M == 1:
    print(3)
elif M == 4:
    print(4)
elif M%5 == 1 or M%5 == 3:
    print(v5+1)
else:
    print(v5+2)
  
