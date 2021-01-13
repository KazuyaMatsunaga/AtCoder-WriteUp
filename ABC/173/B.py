N = int(input())
S = [input() for i in range(N)]

count = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}

for i in S:
    count[i] += 1

ans = 'AC x ' + str(count['AC']) + '\n' + 'WA x ' + \
    str(count['WA']) + '\n' + 'TLE x ' + str(count['TLE']) + \
    '\n' + 'RE x ' + str(count['RE'])

print(ans)
