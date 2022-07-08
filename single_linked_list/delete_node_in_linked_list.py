class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    # Create a Linked List
    def create_linked_list(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    # Display Your Linked List
    def display(self):
        if self.head is None:
            print("\n Linked-List is empty !")
        temp = self.head
        while temp:
            print(temp.data, end="--->")
            temp = temp.next

    # Delete a Given Node
    def delete(self, key):
        if self.head.data == key:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next is not None:
                if temp.next.data == key:
                    temp.next = temp.next.next
                    break
                else:
                    temp = temp.next


if __name__ == "__main__":
    obj = LinkedList()
    num = 0
    while num >= 0:
        num = int(input("Enter a number : "))
        if num < 0:
            break
        else:
            obj.create_linked_list(num)

    print("\n **************Single Linked List***************\n")
    obj.display()
    val = int(input("\n Enter the no has to be deleted the Node : "))
    obj.delete(val)
    print("\n **************Single Linked List***************\n")
    obj.display()

# ----------------Written By : - Aditya Pratap Singh ------------------