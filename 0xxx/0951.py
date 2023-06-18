n = int(input())

ch1 = n // 1000
ch2 = n // 100 % 10
ch3 = n // 10 % 10
ch4 = n % 10

res = ch1 * 1000 + ch3 * 100 + ch2 * 10 + ch4

print(res)
