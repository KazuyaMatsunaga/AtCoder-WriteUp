N, A, B = map(int, input().split())

sum = 0

for i in range(N):
    sum_t = 0
    j = i + 1
    n = j
    while n != 0:
        sum_t += n % 10
        n //= 10
    if sum_t >= A and sum_t <= B:
        sum += j

print(sum)
