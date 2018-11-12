# A clerk works in a store where the cost of each item is a positive integer number of dollars. So, for example, something might cost  21,butnothingcosts21,butnothingcosts 9.99. In order to make change a clerk has an unbounded number of bills in each of the following denominations:  1,1, 2,  5,5, 10, and $20. Write a procedure that takes two arguments, the cost of an item and the amount paid, and prints how to make change using the smallest possible number of bills.

def make_change(cost, paid):
    global start_change, result
    change = paid - cost
    start_change = change
    money = (20, 10, 5, 2, 1)
    index = 0
    result = {}
    
    if change >= 1:
        while change != 0:
            if change // money[index] >= 1:
                result[money[index]] = change // money[index]
                change %= money[index] 
            index += 1        
    else:
        print('Change is not needed')
    return result


# Tests
make_change(5, 5)
make_change(1, 109)

if start_change >= 1:
    for bills, count in result.items():
        print('Need {} bills for ${}.'.format(count, bills))
