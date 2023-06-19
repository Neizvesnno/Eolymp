my_string = input()

start = -1
count = 0
while True:
    start = my_string.find("5", start+1)
    if start == -1:
        break
    count += 1
  
print(count)
