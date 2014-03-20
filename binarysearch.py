

def binarysearch(_list, _v, _min = 0, _max = None):
    
    if _max == None:
        _max = len(_list)
        if _max == 0:
            return False

    middle_index = (_min + _max)/2
    middle = _list[middle_index]

    if _min == _max:
        return False

    if _min == _max - 1:
        if _v == middle:
            return middle_index
        return False

    
    else: 

        if _v < middle:
            return binarysearch(_list, _v, _min, middle_index)
        
        return binarysearch(_list, _v, middle_index, _max)
         


