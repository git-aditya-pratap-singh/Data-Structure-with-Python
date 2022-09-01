class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class Tree:
    # Create A Tree
    def insertNode(self, node, data):
        if node is None:    # root.data == None
            return Node(data) 

        elif node.data < data:
            node.right = self.insertNode(node.right, data)    # the address of node.right transfer to node !

        elif node.data > data:
            node.left = self.insertNode(node.left, data)    # the address of node.left transfer to node !

        return node

    # Inorder Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end="----> ")
            self.inorder(root.right)

    # Preorder Traversal
    def preorder(self, root):
        if root:
            print(root.data, end="----> ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder Traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end="----> ")


if __name__ == "__main__":
    obj = Tree()
    root = None
    while True:
        num = int(input("\n Enter the Data into Tree (Node) : "))
        if num < 0:
            break
        else:
            root = obj.insertNode(root, num)

    print("\n ------------ In-Order Traversal -------------\n")
    obj.inorder(root)

    print("\n ------------ Pre-Order Traversal -------------\n")
    obj.preorder(root)

    print("\n ------------ Post-Order Traversal -------------\n")
    obj.postorder(root)

# ---------------- Written By : - Aditya Pratap Singh ------------------
