arr_results = []

while True:
    a, b, c = map(int, input().split())
    s, d, f = a*a, b*b, c*c

    if a == 0 and b == 0 and c == 0:
        break

    if s + d == f or s + f == d or d + f == s:
        arr_results.append('right')
    else:
        arr_results.append('wrong')

for i in arr_results:
    print(i)
