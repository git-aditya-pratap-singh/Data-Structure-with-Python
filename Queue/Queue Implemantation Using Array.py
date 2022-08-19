class Queue:
    def __init__(self, size):
        self.arr = [None]*size  # arr = [None, None, None] if size = 3
        self.front = 0
        self.rear = 0
        self.size = size

    # Enqueue element on the Queue
    def enqueue(self, data):
        if self.rear == self.size:
            print("\n Queue if Full (Overflow) !")
        else:
            self.arr[self.rear] = data
            self.rear += 1

    # DeQueue element on the Queue
    def dequeue(self):
        if self.front == self.rear:
            print("\n------> Queue is Underflow !")
        else:
            print("\n Dequeue Element : ", self.arr[self.front])
            self.front += 1

    # Display a Queue
    def display(self):
        if self.rear == 0:
            print("\n Queue is empty !")
        else:
            print('\n ----- Queue -----')
            for i in range(self.front, self.rear):
                print(self.arr[i], end=" | ")


if __name__ == "__main__":
    size_arr = int(input("\n Enter the size of Array : "))
    obj = Queue(size_arr)
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
