

def mergetwo(_left, _right):
    result = []
    _l,_r = (0, 0)
    _max_l = len(_left)
    _max_r = len(_right)

    while _l < _max_l and _r < _max_r:
        if _left[_l] < _right[_r]:
            result.append(_left[_l])
            _l += 1
        else:
            result.append(_right[_r])
            _r += 1

    if _l == _max_l:
        while _r < _max_r:
            result.append(_right[_r])
            _r += 1
    else: 
        while _l < _max_l:
            result.append(_left[_l])
            _l += 1
    
    return result

def mergesort(_list):
    #print(_list)    
    _max = len(_list)
    
    if _max == 0:
        return False 

    if _max == 1:
        return _list
    
    middle = _max / 2
    
    return mergetwo(mergesort(_list[:middle]), mergesort(_list[middle:]))


