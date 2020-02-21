import collections

N = int(input())
A = [int(input()) for i in range(N)]

count_dict = collections.Counter(A)

# print(count_dict)

count = 0

for i in count_dict.values():
    if i % 2 == 1:
        count += 1

print(count)
