n = str(input())
count = 0

for i in range(0, len(n)):
    if n[i] == "a":
        print(i, end=" ")
        count += 1

if count == 0:
    print(-1)
  
