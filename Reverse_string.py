#1. Строка в обратной последовательности

def reverse(s):
    '''String reverse'''
    b = list(s)
    i = 0
    k = len(s) - 1
    n = 0
    
    while n < len(s)/2:
        b[i], b[k] = b[k], b[i]
        i += 1
        k -= 1
        n += 1
    return ''.join(b)


assert reverse('abcde') == 'edcba'
assert reverse('abcd') == 'dcba'

s1 = 'Dima'
s2 = 'Dmytruk'
print('Original: {}. Reversed: {}!'.format(s1, reverse(s1)))
print('Original: {}. Reversed: {}!'.format(s2, reverse(s2)))