r,w,i = map(int,input().split())

vid = r*2

if vid >= (w**2+i**2)**0.5:
    print("YES")
else:
    print("NO")
