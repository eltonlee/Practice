

def nested_sum(L):
    if type(L) == int:
        return L
    elif type(L) == float:
        return 0
    elif L == None:
        return 0
    elif len(L) == 0:
        return 0
    elif type(L) == list:
        return nested_sum(L[0]) + nested_sum(L[1:])
    else:
        return 0


L = [[1,2,3,'a'], [4,5.0,None, [] ]]
print(nested_sum(L))
