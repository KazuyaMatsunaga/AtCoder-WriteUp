N = int(input())
A = [int(i) for i in input().split()]
An = A

while len(An) > 2:
    L = len(An)
    winners = []
    for j in range(L // 2):
        first = An[2 * j]
        second = An[2 * j + 1]
        if first > second:
            win = first
        else:
            win = second
        winners.append(win)
    An = winners

print(A.index(min(An)) + 1)
