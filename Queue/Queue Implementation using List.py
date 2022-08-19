class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0

    # EnQueue element on the Queue
    def enqueue(self, data):
        self.rear += 1
        self.queue.append(data)

    # DeQueue element on the Queue
    def dequeue(self):
        if self.queue == []:
            print("\n ---> Queue is empty !")
        else:
            print("Dequeued Element : ", self.queue[self.front])
            self.queue.pop(self.front)

    # Display a Queue
    def display(self):
        if self.rear == 0:
            print("\n ------> Queue is empty !")
        else:
            print('\n ----- Queue -----')
            for i in self.queue:
                print(i, end=" | ")


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
            obj.dequeue()
        else:
            break
    obj.display()

# ---------------- Written By : - Aditya Pratap Singh ------------------

'''Applications of Queue : ---------->
   1. CPU scheduling, Disk Scheduling
   2. Call Center phone systems use Queues to hold people calling them in order.'''