class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Create a Circular Linked List
    def create_linked_list(self, data):
        if self.head is None:
            newnode = Node(data)
            self.head = newnode
            newnode.next = self.head
        else:
            temp = self.head
            while True:
                if temp.next == self.head:
                    newnode = Node(data)
                    temp.next = newnode
                    newnode.next = self.head
                    break
                else:
                    temp = temp.next

    # Insert a new Node at Ending
    def insert_node_at_ending(self, data):
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        newnode = Node(data)
        temp.next = newnode
        newnode.next = self.head


    # Display a Circular Linked List
    def display(self):
        temp = self.head
        while True:
            print(temp.data, end="--->")
            temp = temp.next
            if temp == self.head:
                break


if __name__ == "__main__":
    obj = CircularLinkedList()
    num = 0
    while num >= 0:
        num = int(input(" Enter the Numbers : "))
        if num < 0:
            break
        else:
            obj.create_linked_list(num)

    print("\n************** Circular Linked List ***************\n")
    obj.display()
    num = int(input("\n Enter the New Node at Ending : "))
    obj.insert_node_at_ending(num)
    print("\n************** Circular Linked List ***************\n")
    obj.display()

# ---------------- Written By : - Aditya Pratap Singh ------------------
