from collections import Counter

w = input()

count = Counter(w)

judge = True

for v in count.values():
    if v % 2 == 1:
        judge = False

if judge:
    print("Yes")
else:
    print("No")
