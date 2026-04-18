"""
з умови
Three variants of tree nodes' vivsiting using recursion
"""
class Node:
    """Node class"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order(node: Node):
    """pre-order node visiting"""
    final = []
    if node is not None:
        final.append(node.data)
        final += pre_order(node.left)
        final += pre_order(node.right)
    return final

# In-order traversal
def in_order(node: Node):
    """in-order node visiting"""
    final = []
    if node is not None:
        final += in_order(node.left)
        final.append(node.data)
        final += in_order(node.right)
    return final

# Post-order traversal
def post_order(node: Node):
    """post-order node visiting"""
    final = []
    if node is not None:
        final += post_order(node.left)
        final += post_order(node.right)
        final.append(node.data)
    return final
