n = str(input())

n = n.replace(" ","")
smrl = n[::-1]

if n == smrl:
    print("YES")
else:
    print("NO")
  
