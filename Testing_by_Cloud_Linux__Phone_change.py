#your monthly phone bill has just arrived, and it's unexpectedly large. you decide to verify the amount by recalculating the 
#bill based on your phone call logs and the phone company's charges

import operator
from math import ceil


s ='''00:01:07, 400-234-090
    00:05:01, 701-080-080
    00:05:00, 400-234-090'''


numbers = {}
a = []
s = s.replace('\n', ';')
s = s.replace(' ', '')

for i in s.split(';'):
    a.append(i)


b = []
for i in a:
    i = i.split(',')
    b.append(i)

i = 0
m = []
while i < len(b):
    for z in b[i]:
        z = z.split(':')
        m.append(z)
    i += 1
# print(m)

for i in range(0, len(m), 2):
    m[i] = int(m[i][0])*3600 + int(m[i][1])*60 + int(m[i][2])
# print(m)

x = 0
while x < len(m)-1:
    if str(m[x+1]) not in numbers:
        m[x], m[x+1] = m[x+1], m[x]
    x += 1
# print(m)

for i in range(0, len(m), 2):
    if tuple(m[i]) not in numbers:
        numbers[tuple(m[i])] = m[i-1]
    else:
        numbers[tuple(m[i])] += m[i-1]
# print(numbers)

sorted_x = sorted(numbers.items(), key=operator.itemgetter(1))
sorted_x.pop(-1)
# print(dict(sorted_x))

total = 0
for k, v in dict(sorted_x).items():
    if 0 < v < 300:
        total += v * 3
    elif v >= 300:
        total += ceil(v / 60) * 150
        
print(total)