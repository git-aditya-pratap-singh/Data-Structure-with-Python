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
            newnode.prev = newnode
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            newnode = Node(data)
            newnode.next = temp.next
            temp.next = newnode
            newnode.prev = temp
            self.tail = newnode

    # Delete a Node

    def delete(self, key):
        if self.head.data == key and self.head.next == self.head:
            self.head = None
        elif self.head.data == key:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            self.head = self.head.next
            temp.next = self.head
        else:
            temp = self.head
            while True:
                if temp.data == key:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    break
                temp = temp.next

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
    val = int(input("\n Enter the no has to be deleted the Node : "))
    obj.delete(val)
    print("\n************** Circular Doubly Linked List ***************\n")
    obj.display()

# ---------------- Written By : - Aditya Pratap Singh ------------------
