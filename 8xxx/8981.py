n = str(input())

first = n.find(" ")
last = n.rfind(" ")

if first == -1:
    print(-1)
else:
    print(first, last)
  
