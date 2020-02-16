import collections

N = int(input())
S = [input() for i in range(N)]

# print(S)

count = collections.Counter(S)

# print(count)

max_value = max(count.values())

max_k_list = []

for k, v in sorted(count.items(), key=lambda x: x[1], reverse=True):
    if v == max_value:
        max_k_list.append(k)
    else:
        break

max_k_list.sort()

for i in max_k_list:
    print(i)
