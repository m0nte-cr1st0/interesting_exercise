# Целью данного задания является разработка циклического шифрования сообщений.
# Данный тип шифра использовался Юлием Цезарем для переписки с его генералами.
# Он является достаточно простым для генерации и может быть легко расшифрован и, потому, не предоставляет нужной степени надежности.

phrase = input('Enter sentence to encrypt: ')
shift = int(input('Enter shift value: '))
n = 0
new_phrase = []


while n < len(phrase):
    if phrase[n].isalpha():
        if phrase[n].islower():
            if 0!= ord('z') - (ord(phrase[n]) % (ord('z'))) > shift:
                new_phrase.append(chr(ord(phrase[n])+shift))
            else:
                new_phrase.append(chr(ord('a')+ord(phrase[n])+shift-1-ord('z')))
        else:
            if 0 != ord('Z') - (ord(phrase[n]) % (ord('Z'))) > shift:
                new_phrase.append(chr(ord(phrase[n])+shift))
            else:
                new_phrase.append(chr(ord('A')+ord(phrase[n])+shift-1-ord('Z')))
    else:
        new_phrase.append(phrase[n])
    n += 1

print('The encoded phrase is: ', end='')
for i in new_phrase:
    print(i, end='')