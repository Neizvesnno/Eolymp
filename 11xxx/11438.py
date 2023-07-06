n = int(input())

arr_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
arr_res = []
res = 0

while True:
    str_zap = str(input())
    
    for i in str_zap:
        if i in arr_numbers:
            res += 1

    arr_res.append(res)
    res = 0
    
    n -= 1
    if not n:
        break
        
for i in arr_res:
    print(i)
  
