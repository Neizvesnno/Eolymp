n = int(input())
arr = []

while True:
    arr.append(str(input()))
    
    n -= 1
    
    if not n:
        break
    
for zap_chel in arr:
    if float(zap_chel[:3]) >= 3.5 and (zap_chel[4] == "B" or zap_chel[4] == "A"):
        print(1)
    else:
        print(0)
      
