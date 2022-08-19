class Deque:
    def __init__(self, size):
        self.queue = [None]*size  # [None,None,None] if size = 3
        self.size = size
        self.front = -1
        self.rear = -1

    # Insert Data in front of the Queue
    def front_enqueue(self, data):
        if self.front == 0:
            print('\n Deque if full (Overflow) !')

        elif self.front == -1:
            self.front = self.size-1
            self.rear = self.size-1
            self.queue[self.front] = data

        else:
            self.front = self.front - 1
            self.queue[self.front] = data

    # Insert Data in rear of the Queue
    def rear_enqueue(self, data):
        if self.rear == self.size-1:
            print('\n Deque if full (Overflow) !')

        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data

        else:
            self.rear = self.rear + 1
            self.queue[self.rear] = data

    # Delete Data in front of the Queue
    def front_dequeue(self):
        if self.front == -1:
            print('\n Deque is empty (Underflow) !')

        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp

        else:
            temp = self.queue[self.front]
            self.front += 1
            return temp

    # Delete Data in front of the Queue
    def rear_dequeue(self):
        if self.front == -1:
            print('\n Deque is empty (Underflow) !')

        elif self.front == self.rear:
            temp = self.queue[self.rear]
            self.front = -1
            self.rear = -1
            return temp

        else:
            temp = self.queue[self.rear]
            self.rear -= 1
            return temp

    # Display your Queue
    def display(self):
        print('\n ----- Queue -----')
        if self.rear == -1:
            print("\n Deque is empty !")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" | ")
        print()


if __name__ == "__main__":
    size = int(input("\n Enter the size of Array (Deque) : "))
    obj = Deque(size)

    while True:
        choice = int(input("\n Please ! choose any one concept : \n 1. Insert Data into Front \n 2. Insert Data into Rear \n"))

        if choice == 1:
            while True:
                num = int(input("\n Enter the Number into CircularQueue : "))
                if num < 0:
                    break
                else:
                    obj.front_enqueue(num)
            obj.display()
            break

        elif choice == 2:
            while True:
                num = int(input("\n Enter the Number into CircularQueue : "))
                if num < 0:
                    break
                else:
                    obj.rear_enqueue(num)
            obj.display()
            break

        else:
            print("\n ----> Please ! Select your Right option !")

    while True:
        choice = int(input("\n Please ! choose any one concept : \n 1. Delete Data into Front \n 2. Delete Data into Rear "))

        if choice == 1:
            while True:
                print("\n Please ! Select Your Choice : Y/N ")
                check = input("\n Are You Sure Delete item into Queue : ")
                if check == 'Y':
                    print("------->", obj.front_dequeue())
                else:
                    break
            obj.display()
            break

        elif choice == 2:
            while True:
                print("\n Please ! Select Your Choice : Y/N ")
                check = input("\n Are You Sure Delete item into Queue : ")
                if check == 'Y':
                    print("------->", obj.rear_dequeue())
                else:
                    break
            obj.display()
            break

        else:
            print("\n ----> Please ! Select your Right option !")

# ---------------- Written By : - Aditya Pratap Singh ------------------

'''Applications of Deque Data Structure : ------->
   1. In undo operations on software.
   2. To store history in browsers.'''
