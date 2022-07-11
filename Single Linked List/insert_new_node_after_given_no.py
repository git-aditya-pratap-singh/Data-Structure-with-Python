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
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)

    # Insert New Node after given no
    def insert_node_after_given_no(self, no, data):
        if self.head is None:
            print("\n Linked-list is empty !")
        else:
            temp = self.head
            while temp is not None:
                if temp.data == no:
                    newnode = Node(data)
                    newnode.next = temp.next
                    temp.next = newnode
                    break
                else:
                    temp = temp.next

    # Display Your Linked List
    def display(self):
        if self.head is None:
            print("\n Linked-List is empty !")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end="---->")
                temp = temp.next


if __name__ == "__main__":
    obj = LinkedList()
    num = 0
    while num >= 0:
        num = int(input("Enter the Numbers : "))
        if num < 0:
            break
        else:
            obj.create_linked_list(num)

    no = int(input("\n Enter the given no after insert a node : "))
    val = int(input("\n Enter the given data : "))
    obj.insert_node_after_given_no(no, val)
    print("\n **************Single Linked List***************\n")
    obj.display()

# ----------------Written By : - Aditya Pratap Singh ------------------
