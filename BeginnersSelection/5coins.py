A = int(input())
B = int(input())
C = int(input())
X = int(input())

sum_pair = 0

for a in range(A + 1):
    for b in range(B + 1):
        c = (X - a * 500 - b * 100) / 50
        if c >= 0 and c <= C:
            sum_pair += 1

print(sum_pair)
