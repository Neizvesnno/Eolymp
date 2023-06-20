n = int(input())
if (n%2 == 0 and n>0 and n%3!=0) or (n%2==1 and n<0 and n%3==0) or (n==0):
    print("YES")
else:
    print("NO")
  
