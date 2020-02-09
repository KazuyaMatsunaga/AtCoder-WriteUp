def is_even(num):
    if num % 2 == 0:
        s = 'Even'
        return s
    else:
        s = 'Odd'
        return s

a,b = map(int,input().split())

result = a*b

print(is_even(result))
