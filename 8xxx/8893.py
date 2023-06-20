n = int(input())
a = False
if n%2 == 0 and len(str(abs(n))) == 2 and n%3 == 0:
    a = True
if a == True:
    print("YES")
else:
    print("NO")
  
