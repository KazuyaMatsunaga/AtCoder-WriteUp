N = int(input())

a = list(map(int, input().split()))

sum_alice = 0
sum_bob = 0
a = sorted(a, reverse=True)

for i in range(len(a)):
    if i % 2 == 0:
        sum_alice += a[i]
    else:
        sum_bob += a[i]

print(sum_alice - sum_bob)
