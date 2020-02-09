N = int(input())

A = list(map(int, input().split()))

min = 0

for i in range(N):
    min_t = 0
    while A[i] % 2 == 0:
        A[i] /= 2
        min_t += 1
    if min < min_t:
        min = min_t

print(min)
