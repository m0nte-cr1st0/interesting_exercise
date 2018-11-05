# 2. Консольное меню. Реализуйте программу консольного меню. 
#   2.0. В начале работы программа должна выводить список доступных меню
#   2.1. Программа должна поддерживать 4 пункта меню (1, 2, 3, 4);
#   2.2. Для неверного пункта меню программа должна печатать сообщение об ошибке;
#   2.3. Для каждого из перечисленных в пункте 2.1 меню должна вызываться сотов. подпрограмма (функция) с выводом сообщения о номере выбранного меню.

print('Menu:')
print('     1. Money')
print('     2. Balance')
print('     3. Tickets')
print('     4. Others')
print()

choose = input('Enter number of menu: ')
print()

def f1():
    print('You selected 1. Money.')
def f2():
    print('You selected 2. Balance.')
def f3():
    print('You selected 3. Tickets.')
def f4():
    print('You selected 4. Others.')

if choose == '1':
    f1()
elif choose == '2':
    f2()
elif choose == '3':
    f3()
elif choose == '4':
    f4()
else:
    print('Error. Your choose is false.')