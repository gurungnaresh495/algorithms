

'''This function takes a root node and other two nodes of the same tree and
returns the closest ancestor of both nodes with single traversal'''
def shared_ancestor(root, node1, node2):
    '''Given the root of a binary tree, and two nodes in that tree,
    return the lowest shared ancestor of the two nodes'''

    '''base case'''
    if root is None:
        return root

    '''stops recursion if one of the two nodes is found'''
    if (root.value == node1.value or root.value == node2.value):
        return root

    '''checking frrom both sides'''
    temp1 = shared_ancestor(root.left, node1, node2)
    temp2 = shared_ancestor(root.right, node1, node2)

    '''if both left and right returns node'''
    if temp1 is not None and temp2 is not None:
        return root

    '''if both left and right is null'''
    if temp1 is None and temp2 is None:
        return None
    if temp1 is not None:
        return temp1
    else:
        return temp2