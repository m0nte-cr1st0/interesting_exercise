#Charlemagne, the King of Frankia, is considering building some castles on the border with Servia. The border is divided 
#into N segments. The King knows the height of the terrain in each segment of the border. The height of each segment of 
#terrain is stored in array A, with A[P] denoting the height of the P-th segment of the border. The King has decided to 
#build a castle on top of every hill and in the bottom of every valley.

def solution(A):
    N = len(A)
    P = 1
    Q = N-1
    count = 0

    while P < Q:
        if A[P] > A[P-1]:                  #проверка на холм
            if A[P] == A[P+1]:
                while A[P] == A[P+1]:
                    P += 1
                    if P == Q:             #если больше одной координаты занимает
                        break
            if P != Q and A[P] > A[P+1]:
                count += 1

        elif A[P] < A[P-1]:                #проверка на долину
            if A[P] == A[P+1]:
                while A[P] == A[P+1]:
                    P += 1
                    if P == Q:             #если больше одной координаты занимает
                        break
            if P != Q and A[P] < A[P+1]:
                count += 1
        P += 1
    return count

A = [1, 2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 5]
# A = [-3, -3]

if len(set(A)) == 1:     #Если в множестве будет только 1 элемент - можно построить всего 1 замок
    print(1)
else:
    print(solution(A)+2) #иначе запускаем функцию и +2, так как на углах стоят замки