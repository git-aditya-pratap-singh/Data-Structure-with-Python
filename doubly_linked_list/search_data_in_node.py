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

    # Searching a Node in Doubly Linked List
    def searchkey(self,key):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                return "Found !"
            temp = temp.next
        return "Not Found !"

    # forword direction
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="---->")
            temp = temp.next

if __name__ == "__main__":
    obj = DoublyLinkedList()
    num = 0
    while num >= 0:
        num = int(input(" Enter the number : "))
        if num < 0:
            break
        else:
            obj.create_linked_list(num)

    val = int(input("\n Enter the no search into Node : "))
    print("\n ************** Doubly Linked List ***************\n")
    obj.display()
    print()
    print(obj.searchkey(val))

# ----------------Written By : - Aditya Pratap Singh ------------------
