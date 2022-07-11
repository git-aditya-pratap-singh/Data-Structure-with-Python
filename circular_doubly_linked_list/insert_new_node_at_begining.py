class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Create a Circular Doubly Linked List
    def create_linked_list(self, data):
        if self.head is None:
            newnode = Node(data)
            self.head = newnode
            newnode.next = self.head
            newnode.prev = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            newnode = Node(data)
            newnode.next = temp.next
            temp.next = newnode
            newnode.prev = temp

    # Insert a New Node At Begining
    def insert_node_at_begining(self, data):
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        self.head.prev = newnode
        temp.next = self.head
        newnode.prev = temp.next

    # Display a Circular Doubly Linked List
    def display(self):
        temp = self.head
        while True:
            print(temp.data, end="--->")
            temp = temp.next
            if temp == self.head:
                break


if __name__ == "__main__":
    obj = CircularDoublyLinkedList()
    num = 0
    while num >= 0:
        num = int(input(" Enter the Numbers : "))
        if num < 0:
            break
        else:
            obj.create_linked_list(num)

    print("\n************** Circular Doubly Linked List ***************\n")
    obj.display()
    num = int(input("\n Enter the New Node at Begining : "))
    obj.insert_node_at_begining(num)
    print("\n************** Circular Linked List ***************\n")
    obj.display()

# ---------------- Written By : - Aditya Pratap Singh ------------------
