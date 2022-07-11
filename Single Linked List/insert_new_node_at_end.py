class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert New Node at Ending
    def insert_new_node_at_end(self, data):
        if self.head is not None:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
        else:
            self.head = Node(data)

   # Display your Linked List
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next


if __name__ == '__main__':
    obj = LinkedList()
    obj.insert_new_node_at_end(10)
    obj.insert_new_node_at_end(20)
    obj.insert_new_node_at_end(50)
    print("\n **************Single Linked List***************\n")
    obj.display()

# ----------------Written By : - Aditya Pratap Singh ------------------