n = str(input())

res = str("")

while True:
    if n != "":
        s = n.count(str(n[0]))
        if s > 1:
            res += str(n[0])
    else:
        break
    n = n.replace(str(n[0]), "")

if res == "":
    print("NO")
else:
    print(res)
  
