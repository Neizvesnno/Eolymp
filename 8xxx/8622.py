n = int(input())
ch4 = n // 1000
ch3 = n // 100 % 10
ch2 = n // 10 % 10
ch1 = n % 10
if (ch1 != 0 and ch2 != 0 and ch3 != 0 and ch4 != 0) and n % ch1 == 0 and n % ch2 == 0 and n % ch3 == 0 and n % ch4 == 0:
    print("YES")
else:
    print("NO")
  
