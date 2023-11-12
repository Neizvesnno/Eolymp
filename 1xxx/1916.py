n = str(input())
n = n.lower()
lenner = len(n)

arr = ['a', 'e', 'i', 'o', 'u']
k = 0

for i in n:
    if i in arr:
        k += 1
coly = n.count("y")

upp = lenner - coly - k

if k > upp:
    print('0')
else:
    zxc = 0
    while True:
        k += 1
        zxc += 1
        upp -= 1
        if k > upp:
            break
    print(zxc)
  
