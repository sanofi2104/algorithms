
def bubblesort(_list):
    _max = len(_list) - 1

    if _max == -1:
        return False

    while _max > 0:
        for i in range(_max):
            if _list[i] > _list[i + 1]:
                temp = _list[i]
                _list[i] = _list[i + 1]
                _list[i + 1] = temp

        _max -= 1
    
    return _list
