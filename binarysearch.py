
def binarysearch(_list, _v):
    if len(_list) == 0:
        return False

    elif len(_list) == 1:
        if _list[0] == _v:
            return True
        return False 
     
    else:
        middle_index = len(_list) / 2
        middle = _list[middle_index]

        if _v < middle:
            result = binarysearch(_list[:middle_index], _v)
        
        else:
            result = binarysearch(_list[middle_index:], _v)
        
        return result


