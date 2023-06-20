n = int(input())

ch1 = n // 1000
ch2 = n // 100 % 10
ch3 = n // 10 % 10
ch4 = n % 10

if ch1 == 3 and ch2 == 7 or ch2 == 3 and ch3 == 7 or ch3 == 3 and ch4 == 7:
    print("YES")
else:
    print("NO")
  
