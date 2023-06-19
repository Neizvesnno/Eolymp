n = str(input())

res = 0

while True:
    if n != "":
        n = n.replace(str(n[0]), "")
        res += 1
    else:
        break
   
print(res)
