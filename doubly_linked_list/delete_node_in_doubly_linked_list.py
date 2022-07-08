class Node:
    def __init__(self,data):
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

    # Display a Doubly Linked List
    def display(self):
        if self.head is None:
            print("\n DoublyLinked-List is empty !")
        temp = self.head
        while temp:
            print(temp.data, end="--->")
            temp = temp.next

    # Delete a Given Node
    def delete(self, key):
        temp = self.head
        while temp != None and temp.data != key:
            temp = temp.next
        if temp == None:
            print("Key not found !")
        elif temp == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif temp.next == None:
            temp.prev.next = None
        else:
            temp.prev.next = temp.next 
            temp.next.prev = temp.prev


if __name__ == "__main__":
    obj = DoublyLinkedList()
    num = 0
    while num >= 0:
        num = int(input("\n Enter a number : "))
        if num < 0:
            break
        else:
            obj.create_linked_list(num)

    print("\n ************** Doubly Linked List ***************\n")
    obj.display()
    val = int(input("\n Enter the no has to be deleted the Node : "))
    obj.delete(val)
    print("\n ************** Doubly Linked List ***************\n")
    obj.display()

# ----------------Written By : - Aditya Pratap Singh ------------------