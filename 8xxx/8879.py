a, b, c = map(int, input().split())

if a == b and b == c and a == c:
    print(a + b + c)
elif (a == b and c <= a) or (a == c and b <= c) or (c == b and a <= c):
    print(a + b + c)
elif (b < a < c + b and a > c) or (a < b < c + a and b > c) or (b < c < a + b and c > a):
    print(a + b + c)
else:
    print("No")
  
