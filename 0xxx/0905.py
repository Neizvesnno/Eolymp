a,b,c = map(int,input().split())

if a == b and b == c and a == c:
    print("1")
elif a == b or b == c or a == c:
    print("2")
if a != b and c != a and b != c:
    print("3")
  
