H, W, K = map(int, input().split())
C = [input() for i in range(H)]

# print(C)

black_count = 0

for i in C:
    for j in i:
        if j == "#":
            black_count += 1

# print(black_count)

S = [[], []]

for i in range(len(C)):
    for j in range(len(C[i])):
        S[i].append(C[i][j])

print(S)

S_f = S

zan = K - black_count

zan_re_count = black_count

ans = 0

if zan == zan_re_count:
    ans += 1

for i in range(len(S_f)):
    if zan == zan_re_count - S_f[i].count("#"):
        ans += 1

for i in range(len(S_f)):
    for j in range(len(i)):
        j_black_count = 0
        if S_f[i][j] == "#":
            j_black_count += 1
        if zan == zan_re_count - S_f[i].count("#") - j_black_count:
            ans += 1

            if S_f[i][j] == "#":
                if zan == zan_re_count - i.count("#") - 1:
                    ans += 1
            elif zan == zan_re_count - i.count("#"):
                ans += 1
