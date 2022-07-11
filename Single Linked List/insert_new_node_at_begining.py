class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert Node at Begining
    def insert_node_at_begining(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    # Display your Linked List
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next


if __name__ == '__main__':
    obj = LinkedList()
    obj.head = Node(10)
    ob = Node(20)
    obj.head.next = ob
    obj.insert_node_at_begining(50)
    print("\n **************Single Linked List***************\n")
    obj.display()

# ----------------Written By : - Aditya Pratap Singh ------------------
