import re

S = input()

print(re.sub("[^\t\n\r\f\v]", "x", S))
