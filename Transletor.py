s = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj'
b = ''

for i in s:
    if i.isalpha() and i != 'y' and i != 'z' and i != 'Y' and i != 'Z':
        b += chr(ord(i)+2)
    elif ord(i) % ord('z') == ord('y'):
        b += 'a'
    elif ord(i) % ord('z') == 0:
        b += 'b'
    elif ord(i) % ord('Z') == ord('Y'):
        b += 'A'
    elif ord(i) % ord('Z') == 0:
        b += 'B'
    else:
        b += chr(ord(i))
print(b)