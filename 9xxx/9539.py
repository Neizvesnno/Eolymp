a, b, c = map(int, input().split())

sh = a - b # шляпа
kabl = a - c
res = a - sh - kabl

if res > 0 and res <= 200:
    print(res)
  
