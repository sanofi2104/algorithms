

def insertionsort(_list):

    _max = len(_list)

    if _max == 0:
        return False

    if _max == 1:
        return _list

    for i in range(_max - 1):
        if _list[i] > _list[i + 1]:
            
            j = i
            
            while _list[j] > _list[j + 1] and j > 0:
                temp = _list[j]
                _list[j] = _list[j + 1]
                _list[j + 1] = temp
                j -= 1
            
        
    return _list


