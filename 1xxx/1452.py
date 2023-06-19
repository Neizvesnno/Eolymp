q = int(input())
w = int(input())

e = 1

if 2**q < w:
    print(2**q)
else:
    for x in range(q):
        if e > w:
            e -= w
        e += e
    print(e)
  
