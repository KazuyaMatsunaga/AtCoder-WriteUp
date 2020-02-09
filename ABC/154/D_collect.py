N, K = map(int, input().split())
p = list(map(int, input().split()))

for i in range(len(p)):
    p[i] = (p[i] + 1) / 2

sum = 0
S = [0]

for i in p:
    sum += i
    S.append(sum)

# print(S)

max = 0

for i in range(len(p) - K + 1):
    s = S[i + K] - S[i]
    # print(s)
    if max < s:
        max = s

print(max)
