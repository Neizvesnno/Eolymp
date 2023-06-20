a, b = map(int, input().split())

list_chelsy = []

for i in range(a, b + 1):
    if i % 2 == 0:
        list_chelsy.append(i)
        
maximum = len(list_chelsy)
        
for i in reversed(range(0, maximum)):
    print(list_chelsy[int(i)], end=" ")
  
