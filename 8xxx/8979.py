n = input()
res = 0
s = -1
while True:
    s = n.find("a", s+1)
    if s == -1:
        break
    res += 1
if res >= 1:
    print("a"*res)
else:
    print(-1)
  
