class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Create A Linked List
    def createList(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)

    # Display A Linked List
    def display(self):
        if self.head is None:
            print("\n LinkedList is Empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end="--->")
                temp = temp.next

    # Insert New Node at given Position
    def insert_node_at_mid(self, pos, data):
        if self.head is None:
            print("\n LinkedList is empty")
        else:
            count = 1
            temp = self.head
            while temp is not None:
                if count == pos:
                    print(count)
                    newnode = Node(data)
                    newnode.next = temp.next
                    temp.next = newnode
                    break
                else:
                    count += 1
                    temp = temp.next


if __name__ == '__main__':
    obj = LinkedList()
    num = 0
    while num >= 0:
        num = int(input("\n Enter the numbers : "))
        if num < 0:
            break
        else:
            obj.createList(num)

    val = int(input("\n Enter the position at insert a Node : "))
    data = int(input("\n Enter the Data in a Node : "))
    obj.insert_node_at_mid(val, data)
    print("\n **************Single Linked List***************\n")
    obj.display()

# ----------------Written By : - Aditya Pratap Singh ------------------
