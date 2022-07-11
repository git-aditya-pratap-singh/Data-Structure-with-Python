class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Create a Doubly Linked List
    def create_linked_list(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            newnode = Node(data)
            temp.next = newnode
            newnode.prev = temp
            self.tail = newnode

    #Insert a New Node before a given no
    def insert_node_before_given_no(self,key,data):
        if self.head.data == no:
            newnode = Node(data)
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        else:
            temp = self.head
            while temp is not None:
                if temp.next.data == key:
                    newnode = Node(data)
                    newnode.next = temp.next
                    temp.next.prev = newnode
                    newnode.prev = temp
                    temp.next = newnode
                    break
                else:
                    temp = temp.next

    # Display a Doubly Linked List
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="---->")
            temp = temp.next

    # Display a Doubly Linked List in Reverse
    def reverse_display(self):
        temp = self.tail
        while temp is not None:
            print(temp.data, end="---->")
            temp = temp.prev


if __name__ == "__main__":
    obj = DoublyLinkedList()
    num = 0
    while num >= 0:
        num = int(input("\n Enter the number : "))
        if num < 0:
            break
        else:
            obj.create_linked_list(num)

    print("\n ************** Doubly Linked List ***************\n")
    obj.display()
    no = int(input("\n Enter the given no before insert a node : "))
    val = int(input("\n Enter the given data : "))
    obj.insert_node_before_given_no(no, val)
    print("\n ************** Doubly Linked List ***************\n")
    obj.display()
    print("\n ************** Doubly Linked List in Reverse ***************\n")
    obj.reverse_display()

# ----------------Written By : - Aditya Pratap Singh ------------------
