from __future__ import print_function

class TreeNode:
    def __init__(self, v, l=None, r=None):
        self.value = v
        self.left = l
        self.right = r

def tree_insert(root, x):
    attr = 'left' if x < root.value else 'right'
    side = getattr(root, attr)
    if not side: setattr(root, attr, TreeNode(x))
    else: tree_insert(side, x)

def print_tree(root):
    if root is None:
        return
    print(root.value, end=' - ')
    print_tree(root.left)
    print_tree(root.right)

if __name__ == '__main__':
    root = TreeNode(7)

    tree_insert(root, 4)
    tree_insert(root, 5)
    tree_insert(root, 8)
    tree_insert(root, 9)
    tree_insert(root, 2)
    tree_insert(root, 3)

    print_tree(root) # outputs: 7 - 4 - 2 - 3 - 5 - 8 - 9 -
    