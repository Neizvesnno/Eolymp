n = int(input())

ch5 = n // 10000
ch4 = n // 1000 % 10
ch3 = n // 100 % 10
ch2 = n // 10 % 10
ch1 = n % 10

if ch5 == ch4 or ch5 == ch3 or ch5 == ch2 or ch5 == ch1:
    print("YES")
elif ch4 == ch3 or ch4 == ch2 or ch4 == ch1:
    print("YES")
elif ch3 == ch2 or ch3 == ch1:
    print("YES")
elif ch2 == ch1:
    print("YES")
else:
    print("NO")
  
