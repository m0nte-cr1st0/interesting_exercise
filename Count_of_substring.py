s = 'azcbobobegghakl'
f = 'bob'
n, count = 0, 0


while n <= (len(s) - len(f)):
    i, k = n, 0
    while k < len(f):
        if s[i] == f[k]:
            i += 1
            k += 1
        else:
            break
    else:
        count += 1
    n += 1

print(count)