n = str(input())

count = 0
founder = 0

while True:
    zapper = n[0]

    if zapper == "f":
        count += 1

    n = n[1::]

    if not n or count == 2:
        break

    founder += 1

if count == 0:
    print(-2)
elif count == 1:
    print(-1)
else:
    print(founder)
  
