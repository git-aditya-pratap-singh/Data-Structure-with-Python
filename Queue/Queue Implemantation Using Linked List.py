class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    # EnQueue element on the Queue
    def enqueue(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    # DeQueue element on the Queue
    def dequeue(self):
        if self.head is None:
            print("\n Queue is empty !")
        else:
            temp = self.head.data
            self.head = self.head.next
            return temp

    # Display a Queue
    def display(self):
        print("\n ********* Display Queue *********")
        if self.head is None:
            print("\n Queue is empty !")
        temp = self.head
        while temp:
            print(temp.data, end=" | ")
            temp = temp.next


if __name__ == "__main__":
    obj = Queue()
    num = 0
    while num >= 0:
        num = int(input("\n Enter the Number into Queue : "))
        if num < 0:
            break
        else:
            obj.enqueue(num)
    obj.display()
    while True:
        print("\n Please ! Select Your Choice : Y/N ")
        check = input("\n Are You Sure Delete item into Queue : ")
        if check == 'Y':
            print("Dequeue element : ", obj.dequeue())
        else:
            break
    obj.display()

# ---------------- Written By : - Aditya Pratap Singh ------------------

'''Applications of Queue : ---------->
   1. CPU scheduling, Disk Scheduling
   2. Call Center phone systems use Queues to hold people calling them in order.'''