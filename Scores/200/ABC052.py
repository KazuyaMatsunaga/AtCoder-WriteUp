N = int(input())
S = input()

x = 0

max = x

for s in S:
    if s == 'I':
        x += 1
    else:
        x -= 1
    if max < x:
        max = x

print(max)
