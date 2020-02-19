s = input()

A = s.find('A')

i = 0

for s_i in reversed(s):
    if s_i == 'Z':
        break
    i += 1

Z = len(s) - i - 1

print(Z-A+1)
