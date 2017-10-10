'''
- node: The index of the node you want the parent of.
- size: The index of the root node
'''
def getParent(node, size):
    rank = size
    index = size
    while (rank > 0):
        leftIndex = index - (rank + 1)/2
        rightIndex = index - 1

        if (node == leftIndex or node == rightIndex):
            return index

        index = (leftIndex if (node < leftIndex) else rightIndex)
        rank  = (rank - 1)/2


'''
Inputs:
    (int) h = 3
    (int list) q = [7, 3, 5, 1]
Output:
    (int list) [-1, 7, 6, 3]
'''
def answer(h, q):
    p = [] 
    root_index = (2 ** h) - 1
    for i in range(len(q)):
        parent = getParent(q[i],root_index)
        if(parent is None):
            p.append(-1)
        else:    
            p.append(parent)
    return p

h = 5
print(answer(h,[19, 14, 28]))