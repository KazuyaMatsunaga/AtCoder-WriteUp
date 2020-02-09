N = int(input())
K = int(input())
X = int(input())
Y = int(input())

sum = 0

for i in range(N):
    if i <= K - 1:
        sum += X
    else:
        sum += Y

print(sum)
