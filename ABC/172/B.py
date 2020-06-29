S = input()
T = input()

ans = 0

if S == T:
    ans = 0
else:
    for i, j in zip(S, T):
        if i != j:
            ans += 1

print(ans)
