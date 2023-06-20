a,b = map(int,input().split())

for res in range(a, b + 1):
    print(res*res, end=" ")

print()

for res in reversed(range(a, b + 1)):
    print(res**3, end=" ")
  
