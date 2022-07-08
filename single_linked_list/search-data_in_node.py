class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Searching a Node
    def search_key(self, key):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                return "Found!"
            temp = temp.next
        return "Not Found!"


if __name__ == '__main__':
    obj = LinkedList()
    obj.head = Node(10)
    e2 = Node(20)
    obj.head.next = e2
    e2.next = Node(30)
    print("\n **************Single Linked List***************\n")
    print(obj.search_key(10))

# ----------------Written By : - Aditya Pratap Singh ------------------
    