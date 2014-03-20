
def bubblesort(_list):
    _max = len(_list) - 1

    if _max == -1:
        return False

    while _max > 0:
        flag = False 

        for i in range(_max):
            if _list[i] > _list[i + 1]:
                flag = True
                temp = _list[i]
                _list[i] = _list[i + 1]
                _list[i + 1] = temp

        if not flag: 
            break

        _max -= 1
    
    return _list
