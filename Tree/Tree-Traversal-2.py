class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    # Create A Tree
    def createTree(self, val):
        if self.data is None:   # root.data == None
            self.data = val

        elif self.data == val:
            return

        elif self.data > val:
            if self.left:
                self.left.createTree(val)     # the address of self.left transfer to self !
            else:
                self.left = Node(val)

        elif self.data < val:
            if self.right:
                self.right.createTree(val)   # the address of self.right transfer to self !
            else:
                self.right = Node(val)

    # Inorder Traversal
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=" ---> ")
        if self.right:
            self.right.inorder()

    # Preorder Traversal
    def preorder(self):
        print(self.data, end=" ---> ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    # Postorder Traversal
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=" ---> ")


if __name__ == "__main__":
    root = Node(None)  # here One parameter is pass into Node then self.data = None
    while True:
        num = int(input("\n Enter the node into Tree : "))
        if num < 0:
            break
        else:
            root.createTree(num)

    print("\n ------------ In-Order Traversal -------------\n")
    root.inorder()

    print("\n ------------ Pre-Order Traversal -------------\n")
    root.preorder()

    print("\n ------------ Post-Order Traversal -------------\n")
    root.postorder()

# ---------------- Written By : - Aditya Pratap Singh ------------------

