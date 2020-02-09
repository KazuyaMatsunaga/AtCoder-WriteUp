a, b, c = map(int, input().split())

penkis = []
penkis.append(a)
penkis.append(b)
penkis.append(c)

print(len(list(set(penkis))))
