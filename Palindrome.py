def reverse(s):
    '''String reverse'''
    b = list(s)
    i = 0
    k = len(s) - 1
    
    while i < len(s)/2:
        b[i], b[k] = b[k], b[i]
        i += 1
        k -= 1
    return ''.join(b)

def pallindrom(s):
    '''String reverse'''
    new_s = s.lower().replace(' ','')
    i = 0
    k = len(new_s) - 1
    
    while i < len(new_s)/2:
        res = 'Строка "{}" - палиндром!'.format(s)
        if new_s[i] == new_s[k]:
            i += 1
            k -= 1
        else:
            res = 'Строка "{}" - не палиндром! Потому что строка "{}" не равна строке "{}"!'.format(s, s.lower(), reverse(s).lower())
            break
    return res
        

assert pallindrom('abcde') == 'Строка "abcde" - не палиндром! Потому что строка "abcde" не равна строке "edcba"!'
assert pallindrom('abcd') == 'Строка "abcd" - не палиндром! Потому что строка "abcd" не равна строке "dcba"!'
assert pallindrom('Нам сила талисман') == 'Строка "Нам сила талисман" - палиндром!'
assert pallindrom('Мёд ждём') == 'Строка "Мёд ждём" - палиндром!'

print(pallindrom('Abcde'))
print(pallindrom('abcd'))
print(pallindrom('Abba'))
print(pallindrom('abcba'))
