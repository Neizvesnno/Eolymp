n = str(input())

res = "" + n[0]
count = 1

for i in n:
    if count == len(n):
        break
    
    if i == n[count]:
        res += "0"
    else:
        res += "1"
        
    count += 1

print(res)
