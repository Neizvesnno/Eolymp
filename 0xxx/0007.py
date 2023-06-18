n = str(input()).split("+")

res = 0
arr = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
num = [1, 5, 10, 50, 100, 500, 1000]
b_ch = ['I', 'V', "X", "L", "C", "D", "M"]
str_res = ''

for x in n:
    r, p = 0, 0
    for i in range(len(x) - 1, -1, -1):
        c = num[b_ch.index(x[i])]
        if c < p: 
            r -= c
        else: 
            r += c
        p = c
    res += r

for k, v in arr.items():
    while True:
        
        if res < k:
            break
            
        str_res += v
        res -= k
        
print(str_res)
