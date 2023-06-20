n = str(input())

count = 0

N_K = n.count('.')
N_P = n.count('?')
N_O = n.count('!')

N_TK = n.count('...')
N_TP = n.count('???')
N_TO = n.count('!!!')

count = N_K + N_P + N_O - (N_TK * 2 + N_TP * 2 + N_TO * 2)

print(count)
