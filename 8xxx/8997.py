n = str(input())

zap_n = n
zap_letter = n[0]
zap_count = 0
max_count = 0

while True:
    zap_letter = n[0]
    
    zap_count = n.count(str(zap_letter))
    n = n.replace(str(zap_letter), "")
    
    if max_count < zap_count:
        max_count = zap_count
    
    if not n:
        break
    
print(max_count)
    
while True:
    zap_letter = zap_n[0]
    
    if int(zap_n.count(str(zap_letter))) == max_count:
        print(zap_letter, end=" ")
        
    zap_n = zap_n.replace(str(zap_letter), "")
    
    if not zap_n:
        break
      
