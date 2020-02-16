N = int(input())
A = list(map(int, input().split()))

ans = 'APPROVED'

for i in A:
    if i % 2 == 0:
        if not (i % 3 == 0 or i % 5 == 0):
            ans = 'DENIED'
            break

print(ans)
