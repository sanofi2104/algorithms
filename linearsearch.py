

def linearsearch(_list, _v):
    if len(_list) == 0:
        return False

    for i, item  in enumerate(_list):
        if  item == _v:
            return i
    
    return False 


