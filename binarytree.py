import Queue 

class binary_node(object):

    def __init__(self, _value):
        self.value = _value
        self.left = None
        self.right = None
       

'''
Breadth-First search
'''
def breadth_first(_tree):
    if not _tree:
        return False

    result = []
    queue = Queue.Queue()
    queue.put(_tree)

    while not queue.empty():
        temp = queue.get()
        result.append(temp.value)

        if temp.left:
            queue.put(temp.left)
        if temp.right:
            queue.put(temp.right)
        
    return result 
            
'''
Depth-first search 
'''
# Pre-Order depth-first searching algorithm
def pre_order(_node, result = None):
    if _node == None:
        return
    if result is None:
        result = []

    result.append(_node.value)
    pre_order(_node.left, result)
    pre_order(_node.right, result)
    
    return result


# In-Order depth-first searching algorithm
def in_order(_node, result = None):
    if _node == None:
        return
    if result is None:
        result = []
    
    in_order(_node.left, result)
    result.append(_node.value)
    in_order(_node.right, result)
    
    return result


# Post-Order depth-first searching algorithm
def post_order(_node, result = None):
    if _node == None:
        return
    if result is None:
        result = []
    
    post_order(_node.left, result)
    post_order(_node.right, result)
    result.append(_node.value)
    
    return result



