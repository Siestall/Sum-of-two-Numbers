from random import *

a = []
c = []
m = [choice([_ for _ in range(randint(1,20))]) for _ in range(randint(5,21))]

for i in range(len(m)-1):
    b = m[i] + m[i+1]
    a.append(b)

for l in range(len(m)-1):
    c += [m[l]] + [a[l]]

print(m)
print(c + [m[-1]])