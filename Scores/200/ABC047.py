W, H, N = map(int, input().split())

l = [list(map(int, input().split())) for i in range(N)]

coordinate = [[0, 0], [W, H]]

for i in l:
    if i[2] == 1:
        if coordinate[0][0] < i[0]:
            coordinate[0][0] = i[0]
    elif i[2] == 2:
        if coordinate[1][0] > i[0]:
            coordinate[1][0] = i[0]
    elif i[2] == 3:
        if coordinate[0][1] < i[1]:
            coordinate[0][1] = i[1]
    elif i[2] == 4:
        if coordinate[1][1] > i[1]:
            coordinate[1][1] = i[1]

x = coordinate[1][0] - coordinate[0][0]
y = coordinate[1][1] - coordinate[0][1]

if x <= 0 or y <= 0:
    print(0)
else:
    print(x * y)
