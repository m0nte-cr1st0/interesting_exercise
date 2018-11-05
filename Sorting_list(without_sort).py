# Вариант 2.
# users = [("Tom", 19, 80),
#          ("John", 20, 90),
#          ("Jony", 17, 91),
#          ("Jony", 17, 93),
#          ("Json", 21, 85)]
users = [("Tom", 19, 80),
        ("John", 20, 90),
        ("Jony", 17, 85, 'b'),
         ("Jony", 17, 85, 'a'),
         ("Jony", 17, 85, 'c'),
        ("Jony", 18, 93),
         ("Jony", 19, 93),
         ("Jony", 19, 95),
        ("Jony", 18, 87),
         ("Jony", 17, 91),
        ("Json", 21, 85)]

print("Before: {}".format(users))    

def sort_users(users):
    '''Sorting the list.'''
    sorted_users = [list(i) for i in users]
    new_users = []
    k = 0
    
    while True:
        i = 0
        if len(sorted_users) > 1:
            while i <= len(sorted_users)-2:        
                if sorted_users[i][k] < sorted_users[i+1][k]:
                    sorted_users[i], sorted_users[i+1] = sorted_users[i+1], sorted_users[i]
                    i += 1
                    k = 0
                elif sorted_users[i][k] == sorted_users[i+1][k]:
                    k += 1
                else:
                    i += 1
                    k = 0
            new_users.append(tuple(sorted_users[len(sorted_users)-1]))
            sorted_users.pop()
        else:
            new_users.append(tuple(sorted_users[len(sorted_users)-1]))
            break
    return new_users
    
print("After:  {}".format(sort_users(users)))