a = input()
b = input() 
print('Ok' if all([True if a.count(word) >= b.count(word) else False for word in b]) else 'No')
