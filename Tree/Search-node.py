class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    # Create a Tree
    def createTree(self, val):
        if self.data is None:   # root.data == None
            self.data = val

        elif self.data == val:
            return

        elif self.data > val:
            if self.left:
                self.left.createTree(val)    # the address of self.left transfer to self !
            else:
                self.left = Node(val)

        elif self.data < val:
            if self.right:
                self.right.createTree(val)    # the address of self.right transfer to self !
            else:
                self.right = Node(val)

    # Inorder Traversal
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=" ---> ")
        if self.right:
            self.right.inorder()

    # Search a Node in the Tree
    def search(self, key):
        if self.data == key:
            print(f"-----> {key} is Found In the Tree !")

        elif self.data < key:
            if self.right:
                self.right.search(key)
            else:
                print(f"----->{key} is not Found in the Tree !")

        elif self.data > key:
            if self.left:
                self.left.search(key)
            else:
                print(f"-----> {key} is not Found in the Tree !")


if __name__ == "__main__":
    root = Node(None)            # here One parameter is pass into Node then self.data = None
    while True:
        num = int(input("\n Enter the node into Tree : "))
        if num < 0:
            break
        else:
            root.createTree(num)

    print("\n ------------ In-Order Traversal -------------\n")
    root.inorder()

    key = int(input("\n Enter the node searched into the tree : "))
    root.search(key)

# ---------------- Written By : - Aditya Pratap Singh ------------------
