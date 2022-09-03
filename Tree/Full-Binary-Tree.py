class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def CreateTree(self, val):
        if self.data is None:  # root.data == None
            self.data = val

        elif self.data == val:
            return

        elif self.data > val:
            if self.left:
                self.left.CreateTree(val)  # the address of self.left transfer to self !
            else:
                self.left = Node(val)

        elif self.data < val:
            if self.right:
                self.right.CreateTree(val)  # the address of self.right transfer to self !
            else:
                self.right = Node(val)

    def fullBinaryTree(self):

        if self.left is None and self.right is None:
            return True

        elif self.left is not None and self.right is not None:
            return (self.left.fullBinaryTree() and self.right.fullBinaryTree())

        else:
            return False


if __name__ == "__main__":
    root = Node(None)  # here One parameter is pass into Node then self.data = None
    while True:
        num = int(input("\n Enter the node into Tree : "))
        if num < 0:
            break
        else:
            root.CreateTree(num)
    check = root.fullBinaryTree()
    if check is True:
        print("\n -----> This Tree is a Full Binary Tree !")
    else:
        print("\n -----> This Tree is not Full Binary Tree !")

# ---------------- Written By : - Aditya Pratap Singh ------------------
