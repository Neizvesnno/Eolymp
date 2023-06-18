n = int(input())

c = n%10
a = n//100%10
if a > c:
    print(a)
elif a < c:
    print(c)
else:
    print("=")
  
