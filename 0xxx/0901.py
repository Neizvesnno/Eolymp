n = str(input())

n_len = len(n) - 1
i = 0

while True:
    if n[i] == '-' or n[i] == '+' or n[i] == '*' :
        i += 1
    else:
        break
    
while True:
    if n[n_len] == '-' or n[n_len] == '+' or n[n_len] == '*' :
        n_len -= 1
    else:
        break

n = n[i:n_len]

score1 = n.count('-')
score2 = n.count('+')
score3 = n.count('*')

res = score1 + score2 + score3

print(res)
