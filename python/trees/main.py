class TreeNode():
    def __init__(self, x:int):
        self.left = None
        self.right = None
        self.val = x

def insert(node, tree):
    if(node.val < tree.val):
        if tree.left:
            insert(node, tree.left)
        else:
            tree.left = node
    else:
        if tree.right:
            insert(node, tree.right)
        else:
            tree.right = node

def printTree(tree):
    if tree.left:
        printTree(tree.left)

    print(tree.val, end=" ")

    if tree.right:
        printTree(tree.right)

    




def main():
    import random

    root = TreeNode(0)

    for i in range(20):
        insert(TreeNode(random.randint(0,10)), root)

    print(root.val)

    # for i in range(10):
    #     insert(TreeNode(i+1), root)

    printTree(root)


if __name__ == "__main__":
    main()

