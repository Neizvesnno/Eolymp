n = str(input())

n5 = n.count("5")
n2 = n.count("2")

if n5 == n2:
    print("=")
elif n5 > n2:
    print(5)
else:
    print(2)
  
