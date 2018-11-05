def get_anagrams(word, *cont):
    index = 0
    letter = 0
    a = list(word)
    s = list(*cont)
    res = []
    
    while index < len(s):
        while letter < len(s[index]):
            if len(a) == len(s[index]) and s[index][letter] in a and s[index].count(s[index][letter]) == a.count(s[index][letter]):
                letter += 1
            else:
                break
        else:
            letter = 0
            res.append(s[index])
        index += 1
    return res

word = 'heart'
cont = ['earth', 'aaaaa', 'aerth', 'aafasf', 'htrea']
# cont = ['asdfa', 'asffasf']

result = get_anagrams(word, cont)

print('К слову "{}" анаграммой является: {}'.format(word, result))