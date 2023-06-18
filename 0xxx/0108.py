a, b, c = map(int,input().split())

if a < 1000 and b < 1000 and c < 1000:
    if a < b < c or c < b < a:
        print(b)
    elif a < c < b or b < c < a:
        print(c)
    elif b < a < c or c < a < b:
        print(a)
