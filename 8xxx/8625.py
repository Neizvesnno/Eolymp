n = int(input())
ch1 = n // 10
ch2 = (n // 100) * 10 + n % 10
ch3 = n % 100
print(max(ch3, ch2, ch1))
