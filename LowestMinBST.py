class TreeNode:
    '''Node for a simple binary tree structure'''
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

'''Returns a minimum-height BST built from the elements in alist (which are in sorted order)'''
def min_height_BST(alist):
    if len(alist) < 1:
        return None
    else:
        return helperBst(alist, 0, len(alist)-1)

'''helper function '''
def helperBst(lst, a, b):
    if (a > b):
        return None
    m = (a + b)//2
    node = TreeNode(lst[m], None, None)
    node.left = helperBst(lst, a, m-1)
    node.right = helperBst(lst, m+1, b)
    return node