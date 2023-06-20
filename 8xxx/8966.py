n = int(input())
arr = list(map(int, input().split()))[:n:]
arr = arr[::-1]

for i in arr:
    print(i, end=" ")
  
