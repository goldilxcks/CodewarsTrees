"""
Function returning elem of tree by levels
"""
class Node:
    """Node class"""
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node: Node) -> list:
    """Returns the list of elem from trree sorted by levels"""
    if node is None:
        return []
    final_list = [node]
    res = []
    i = 0
    while i < len(final_list):
        current = final_list[i]
        res.append(current.value)
        if current.left:
            final_list.append(current.left)
        if current.right:
            final_list.append(current.right)
        i += 1
    return res
