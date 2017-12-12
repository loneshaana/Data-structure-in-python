# linear search

def linear_search(lst,find):
    for item in lst:
        if find == item:
            return find ,' is in list '
    return find,' is not in a list'
print linear_search([1,2,3,4,5],15)
