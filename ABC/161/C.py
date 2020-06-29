N, K = map(int, input().split())

flag = True

min = N

if K == 1:
    ans = 0
elif N % K == 0:
    ans = 0
elif abs(N - K) > N:
    ans = N
else:
    if (N % K) > (K / 2):
        ans = abs((N % K) - K)
    else:
        ans = N % K

print(ans)
