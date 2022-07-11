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

    # Insert a New Node before a given no
    def insert_node_before_given_no(self, key, data):
        if self.head.data == key:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
            temp.next = newnode
        else:
            temp = self.head
            while True:
                if temp.next.data == key:
                    newnode = Node(data)
                    newnode.next = temp.next
                    temp.next = newnode
                    break
                else:
                    temp = temp.next

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
    no = int(input("\n Enter the given no before insert a node : "))
    val = int(input("\n Enter the given data : "))
    obj.insert_node_before_given_no(no, val)
    print("\n ************** Circular Linked List ***************\n")
    obj.display()

# ---------------- Written By : - Aditya Pratap Singh ------------------
