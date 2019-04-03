class TreeNode:
    '''Node for a simple binary tree structure'''

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

'''This funtion takes tree as a parameter and returns if the tree is Binary Search Tree'''
def isBinarySearchTree(tree):
    if not tree:
        return True
    arr = []
    inorder(arr, tree)
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

'''this function traverses the tree inorder'''
def inorder(array, root):
    if root:
        if root.left:
            inorder(array, root.left)
        array.append(root.value)
        if root.right:
            inorder(array, root.right)
