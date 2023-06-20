n = str(input())

arr = ["1", "3", "5", "7", "9"]
bolleta = False
kk = 0
res = ""

while True:
    for i in range(0, 5):
        kk = arr[i]
        if n[0] == kk:
            bolleta = True
            break
        
    if bolleta == False:
        res = res + n[0]
        
    bolleta = False

    n = n[1::]
    
    if n == "":
        break
        
print(res)
