N, K = map(int, input().split())
p = list(map(int, input().split()))

if N > 1:
    max_p = max(p)
    max_p_index = p.index(max_p)
    # print(max_p_index)
    p = p[max_p_index - (K - 1): max_p_index + (K - 1)]

sum_l = 0
sum_p = 0
sum_p_len = []
max = 0

for i in range(len(p) - K + 1):
    l = p[i:K]
    sum_l = sum(l)
    if max < sum_l:
        max = sum(l)
        sum_p_len = l
    K += 1

# print(sum_p_len)

sum = 0

for i in sum_p_len:
    for j in range(i):
        j += 1
        sum += j / i
    sum_p += sum
    sum = 0

print(sum_p)
