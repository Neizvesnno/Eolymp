n = int(input())

ch3 = n // 100 % 10
ch2 = n // 10 % 10
ch1 = n % 10

maximum = max(ch1, ch2, ch3)
minimal = min(ch1, ch2, ch3)
if maximum == ch1 and minimal == ch3:
    kon = ch2
elif maximum == ch3 and minimal == ch1:
    kon = ch2
elif maximum == ch2 and minimal == ch1:
    kon = ch3
elif maximum == ch1 and minimal == ch2:
    kon = ch3
elif maximum == ch2 and minimal == ch3:
    kon = ch1
elif maximum == ch3 and minimal == ch2:
    kon = ch1
else:
    kon = 0

print((maximum*100+kon*10+minimal)**2)
