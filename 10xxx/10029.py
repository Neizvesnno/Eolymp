a, b, c = map(int, input().split())

if a-b+c == 2020:
    print(f"{a}-{b}+{c}")
elif a-b-c == 2020:
    print(f"{a}-{b}-{c}")
elif a+b-c == 2020:
    print(f"{a}+{b}-{c}")
elif a+b+c == 2020:
    print(f"{a}+{b}+{c}")
else:
    print("CORONA")
  
