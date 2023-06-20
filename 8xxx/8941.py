n,m = map(int,input().split())
sum = 0
for a in range(1, n + 1):
    for b in range(1, m + 1):
        sum = sum + 1
        print(sum, end=" ")
    print()
  
