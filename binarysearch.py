

def binarysearch(_list, _v, _min = 0, _max = None):
    
    if _max == None:
        _max = len(_list)
        if _max == 0:
            return -1

    middle_index = (_min + _max)/2
    middle = _list[middle_index]

    if _min == _max:
        return -1

    if _min == _max - 1:
        if _v == middle:
            return middle_index
        return -1

    
    else: 

        if _v < middle:
            result = binarysearch(_list, _v, _min, middle_index)
        
        else:
            result = binarysearch(_list, _v, middle_index, _max)
        
        return result


