import collections

N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)

sum_dict = {}
sum_dict_n = {}

sum = 0
sum_n = 0

for key in c.keys():
    coll = c[key] * (c[key] - 1) // 2
    sum_dict[key] = coll
    sum += coll
    value_k = c[key] - 1
    coll_n = value_k * (value_k - 1) // 2
    sum_dict_n[key] = coll_n

for a in A:
    ans = sum
    ans = ans - sum_dict[a] + sum_dict_n[a]
    print(ans)
