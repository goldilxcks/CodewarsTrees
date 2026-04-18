# Definition for a binary tree node.
"""Deleting a node in s BST"""
class TreeNode:
    """TreeNode class"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """Solution class"""
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """Function theat deletes a node in a BST"""
        if root is None:
            return None
        i = 0
        curr_list = [(root, None)]
        while i < len(curr_list):
            curr, parent = curr_list[i]
            if curr.val == key:
                if curr.left is not None and curr.right is not None:
                    replace = curr.right
                    new_node = replace
                    while new_node.left is not None:
                        new_node = new_node.left
                    new_node.left = curr.left
                    if parent:
                        if parent.left == curr:
                            parent.left = replace
                        else:
                            parent.right = replace
                    else:
                        return replace
                else:
                    if curr.right is not None:
                        replace = curr.right
                    else:
                        replace = curr.left
                    if parent:
                        if parent.left == curr:
                            parent.left = replace
                        else:
                            parent.right = replace
                    else:
                        return replace
                return root
            if curr.left is not None:
                curr_list.append((curr.left, curr))
            if curr.right is not None:
                curr_list.append((curr.right, curr))
            i += 1
        return root
