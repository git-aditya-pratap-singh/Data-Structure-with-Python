class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # create single linkedList
    def create_linked_list(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    # display LinkedList
    def display(self):
        if self.head is None:
            print("\n Linked-List is empty !")
        temp = self.head
        while temp:
            print(temp.data, end="--->")
            temp = temp.next


if __name__ == '__main__':
    obj = LinkedList()
    num = 0
    while num >= 0:
        num = int(input(" Enter a number : "))
        if num < 0:
            break
        else:
            obj.create_linked_list(num)
    print("\n **************Single Linked List***************\n")
    obj.display()

# ----------------Written By : - Aditya Pratap Singh ------------------


