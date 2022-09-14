class Node:
    def __init__(self, data):
        self.left = None
        self.data = data                  # self.data = None because create an object at a time None arguments passed in constructor
        self.right = None

    def createTree(self, val):
        if self.data is None:
            self.data = val
            return

        elif self.data == val:
            return

        elif self.data > val:
            if self.left:
                self.left.createTree(val)         # the address of self.left transfer to self !
            else:
                self.left = Node(val)

        elif self.data < val:
            if self.right:
                self.right.createTree(val)           # the address of self.right transfer to self !
            else:
                self.right = Node(val)

    # Level-Order-Traversal (In use BFS(Breadth First Search))
    def levelOrder(self):
        self.level = 1             # declare a level of tree
        Queue = []                 # here, it is Queue
        Queue.append(self)         # Queue is stored first root node address at 0 index
        Queue.append(None)         # Queue is stored is None at 1 index ---> [self,None]

        while Queue != []:         # here, it is check your queue is empty or not
            key = Queue.pop(0)      # here, it's remove element at index 0 and to store a key variable
            if key is not None:       # here, it's key is not None because key is stored a root address
                print(f"Level - {self.level} => {key.data}")

                if key.left is not None:
                    Queue.append(key.left)
                if key.right is not None:
                    Queue.append(key.right)

            else:
                print()    # here, it's used to newline
                self.level += 1
                if Queue == []:   # here, it's Queue is none as --- []
                    break
                else:
                    Queue.append(None)      # here, it's Queue is stored is None ---> [None]


if __name__ == "__main__":
    Queue = []
    root = Node(None)
    while True:
        num = int(input("\n Enter the node into Tree : "))
        if num < 0:
            break
        else:
            root.createTree(num)
    root.levelOrder()

''' Here, it is Called Breadth First Search (BFS) Algorithms in used Tree '''

# ---------------- Written By : - Aditya Pratap Singh ------------------
