from __future__ import print_function

# Binary Tree Node
class TreeNode:
    def __init__(self, v, l=None, r=None):
        self.value = v
        self.left = l
        self.right = r

# insert data to the tree
def tree_insert(root, x):
    attr = 'left' if x < root.value else 'right'
    side = getattr(root, attr)
    if not side: setattr(root, attr, TreeNode(x))
    else: tree_insert(side, x)

# preorder traversal through the tree
def print_tree_preorder(root):
    if root is None:
        return
    print(root.value, end=' - ')
    print_tree_preorder(root.left)
    print_tree_preorder(root.right)

# inorder traversal through the tree
def print_tree_inorder(root):
    if root is None:
        return
    print_tree_inorder(root.left)
    print(root.value, end=' - ')
    print_tree_inorder(root.right)

# postorder traversal through the tree
def print_tree_postorder(root):
    if root is None:
        return
    print_tree_postorder(root.left)
    print_tree_postorder(root.right)
    print(root.value, end = ' - ')

if __name__ == '__main__':          #            Tree Structure
    root = TreeNode(7)              #                 7
    tree_insert(root, 4)            #               /    \
    tree_insert(root, 5)            #             4       8
    tree_insert(root, 8)            #          /    \       \
    tree_insert(root, 9)            #         2      5       9
    tree_insert(root, 2)            #          \
    tree_insert(root, 3)            #           3

    print("Inorder traversal")
    print_tree_inorder(root)        # outputs: 7 - 4 - 2 - 3 - 5 - 8 - 9 -
   
    print("\n\nPreorder traversal")
    print_tree_preorder(root)       # outputs: 7 - 4 - 2 - 3 - 5 - 8 - 9 -
    
    print("\n\nPostorder traversal")
    print_tree_postorder(root)      # outputs: 3 - 2 - 5 - 4 - 9 - 8 - 7 -