print([i for i in ['earth', 'aaaaa', 'aerth', 'aafasf', 'htrea'] if sorted(i) == sorted('heart')])

# Либо
# print((lambda x, y: [i for i in y if sorted(i) == sorted(x)])('heart', ['earth', 'aaaaa', 'aerth', 'aafasf', 'htrea']))