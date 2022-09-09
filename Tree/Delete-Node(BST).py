class Node:
    def __init__(self, data):
        self.left = None
        self.data = data      # self.data = None because create an object at a time None arguments passed in constructor
        self.right = None

    # Create A Binary Search Tree
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
                self.right.createTree(val)    # the address of self.right transfer to self !
            else:
                self.right = Node(val)

    # Display A Tree in (In-Order Traversal)
    def inorder(self):
        if self.left:
            self.left.inorder()       # the address of self.left transfer to self !
        print(self.data, end=" ----> ")
        if self.right:
            self.right.inorder()      # the address of self.right transfer to self !

    def delete(self, key):
        if self.data is None:
            print("\n Binary Search Tree is Empty ! ")
            return

        elif self.data > key:
            if self.left:
                self.left = self.left.delete(key)    # self.left = it's means store an address of return node
            else:
                print("\n Given Node is not present in the Binary Search Tree !")

        elif self.data < key:
            if self.right:
                self.right = self.right.delete(key)    # self.right = it's means store an address of return node
            else:
                print("\n Given Node is not present in the Binary Search Tree !")

        elif self.data == key:
            if self.left is None and self.right is None:    # if the Node are both side is None ( 0 Child)
                return None

            elif self.left is None:   # if the Node are left side is None ( 1 Child)
                return self.right

            elif self.right is None:   # if the Node are right side is None  ( 1 Child)
                return self.left

            else:
                node = self.right       # if the Node are both side is not None  ( 2 Child)
                while node.left:
                    node = node.left
                self.data = node.data
                self.right = self.right.delete(node.data)

        return self   # return self is a root node


if __name__ == "__main__":         # main function()
    root = Node(None)
    while True:
        num = int(input("\n Enter the node into Tree : "))
        if num < 0:
            break
        else:
            root.createTree(num)

    print("\n ------------ In-Order Traversal -------------\n")
    root.inorder()

    key = int(input("\n Delete a Node in Given Binary Search Tree (BST) : "))
    root.delete(key)

    print("\n ------------ In-Order Traversal -------------\n")
    root.inorder()

# ---------------- Written By : - Aditya Pratap Singh ------------------
