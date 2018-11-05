def calculator(C, A, B):
    '''Calculate A and B.'''
    if C == '+':
        print(A + B)
    elif C == '-':
        print(A - B)
    elif C == '*':
        print(A * B)
    elif C == '/' and B == 0:
        print("Деление на 0!")
    elif C == '/' and B != 0:
        print(A / B)
    elif C == 'mod' and B == 0:
        print('Деление на 0!')
    elif C == 'mod' and B != 0:
        print(A % B)
    elif C == 'pow':
        print(A ** B)
    elif C == 'div' and B ==0:
        print('Деление на 0!')
    elif C == 'div' and B != 0:
        print(A // B)
    else:
        print('Error')
    
A = float(input())
B = float(input())
C = str(input())

calculator(C, A, B)