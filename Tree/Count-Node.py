class Node:
    def __init__(self, data):
        self.left = None
        self.data = data            # self.data = None because create an object at a time None arguments passed in constructor
        self.right = None

    def createTree(self, val):
        if self.data is None:
            self.data = val
            return

        elif self.data == val:
            return

        elif self.data > val:
            if self.left:
                self.left.createTree(val)     # the address of self.left transfer to self !
            else:
                self.left = Node(val)

        elif self.data < val:
            if self.right:
                self.right.createTree(val)      # the address of self.right transfer to self !
            else:
                self.right = Node(val)

    # Display A Tree in (In-Order Traversal)
    def inorder(self):
        if self.left:
            self.left.inorder()      # the address of self.left transfer to self !
        print(self.data, end=" ----> ")
        if self.right:
            self.right.inorder()     # the address of self.right transfer to self !

    # Total no of Node In BST
    def Count(self, root):
        if root is None:
            return 0
        return 1 + self.Count(root.left) + self.Count(root.right)   # self address is constant = root node


# Total no of Node In BST
'''def Count_2(node):
    if node is None:
        return 0
    return 1 + Count_2(node.left) + Count_2(node.right)'''


if __name__ == "__main__":
    root = Node(None)
    while True:
        num = int(input("\n Enter the node into Tree : "))
        if num < 0:
            break
        else:
            root.createTree(num)

    print("\n ------------ In-Order Traversal -------------\n")
    root.inorder()
    print("\n Total No. Of Nodes in BST :  ", root.Count(root))
   # print("\n Total No. Of Nodes in BST :  ", Count_2(root))

# ---------------- Written By : - Aditya Pratap Singh ------------------