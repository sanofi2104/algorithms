
def merge(_left, _pivot, _right):
    _left.append(_pivot)

    for i in _right:
        _left.append(i)
    
    return _left 


def quicksort(_list):
    _max = len(_list)

    if _max < 2:
        return _list
    
    pivot_index = _max / 2
    pivot = _list[pivot_index]
    left = []
    right = []

    for i,j in enumerate(_list):
        if i == pivot_index:
            continue

        elif j < pivot:
            left.append(j)
        
        else:
            right.append(j)
     
    return merge(quicksort(left), pivot, quicksort(right))



