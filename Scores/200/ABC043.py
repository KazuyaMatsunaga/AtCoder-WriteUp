s = input()

output = []

for i in s:
    if i != "B":
        output.append(i)
    elif output != []:
        output.pop()

print(''.join(output))
