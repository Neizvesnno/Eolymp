q, w = map(int, input().split())
e = input()

a = int(e, q)
n = ''
x = [10, 11, 12, 13, 14, 15]
c = ['A', 'B', 'C', 'D', 'E', 'F']

if w == 16:
    n = hex(a)
    n = n.upper()
    print(n[2::])
else:
    while a >= w:
        if a % w >= 10:
            n += c[x.index(a % w)]
        else:
            n += str(a % w)
        a = a//w
    n += str(a)
    print(n[::-1])
  
