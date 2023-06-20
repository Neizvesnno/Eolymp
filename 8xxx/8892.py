n = int(input())
a = False
if n%2 != 0 or n > 0 and len(str(abs(n))) == 3:
    a = True
if a == True:
    print("YES")
else:
    print("NO")
  
