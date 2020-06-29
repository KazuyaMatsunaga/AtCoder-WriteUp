N, M = map(int, input().split())
A = list(map(int, input().split()))

sum_a = sum(A)

count = 0

for i in A:
    if i >= (sum_a / (4 * M)):
        count += 1

if count >= M:
    print('Yes')
else:
    print('No')
