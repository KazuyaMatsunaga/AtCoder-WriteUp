K, S = map(int, input().split())

l = []

for i in range(K + 1):
    l.append(i)

count = 0

for i in l:
    for j in l:
        z = S - i - j
        if 0 <= z and z <= K:
            count += 1

print(count)
