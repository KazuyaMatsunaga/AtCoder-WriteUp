import itertools

N, K = map(int, input().split())
A = list(map(int, input().split()))

seki_list = []

for i in itertools.combinations(A, r=2):
    seki_list.append(i[0] * i[1])

seki_list.sort()

print(seki_list)

print(seki_list[K-1])
