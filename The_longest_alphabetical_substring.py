s = 'abcbcd' + ' '
a = ''
b = ''
i = 0


while i <= len(s) - 2:
    if 0 <= ord(s[i+1])-ord(s[i]):
        a += s[i]
    else:
        a += s[i]
        if len(a) > len(b) or len(a) == len(b) and a < b:
            b = a         
        a = ''
    i += 1
    
print(b)