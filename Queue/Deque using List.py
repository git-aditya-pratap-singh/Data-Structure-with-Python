class Deque:
    def __init__(self, size):
        self.queue = []
        self.size = size

    # Insert Data in front of the Queue
    def add_front(self, data):
        if len(self.queue) == self.size:
            print("\n Deque is Full (Overflow) !")
        else:
            self.queue.insert(0, data)
            print("\n ----> Data has be Inserted !")

    # Insert Data in Rear of the Queue
    def add_rear(self, data):
        if len(self.queue) == self.size:
            print("\n Deque is Full (Overflow) !")
        else:
            self.queue.append(data)
            print("\n ----> Data has be Inserted !")

    # Delete Data in front of the Queue
    def remove_front(self):
        if len(self.queue) == 0:
            print("\n Deque is empty (underflow) !")
        else:
            self.queue.pop(0)
            print("\n ----> Data has be deleted !")

    # Delete Data in Rear of the Queue
    def remove_rear(self):
        if len(self.queue) == 0:
            print("\n Deque is empty (underflow) !")
        else:
            self.queue.pop()
            print("\n ----> Data has be deleted !")

    # Display Your Queue
    def display(self):
        print('\n ********* Double Ended Queue *********')
        for i in self.queue:
            print(i, end=" | ")
        print()


if __name__ == "__main__":
    size = int(input("\n Enter the Size of Deque : "))
    obj = Deque(size)

    while True:
        num = int(input("\n Enter the no insert into deque : "))

        choice = int(input("\n Enter Your Choice : \n 1. Add-Front \n 2. Add-Rear \n 3. EXIT \n"))

        if choice == 1:
            obj.add_front(num)
        elif choice == 2:
            obj.add_rear(num)
        elif choice == 3:
            break
        else:
            print("\n Please! Select your Right Option")

    obj.display()

    while True:
        choice = int(input("\n Enter Your Choice : \n 1. Remove-Front \n 2. Remove-Rear \n 3. EXIT \n"))

        if choice == 1:
            obj.remove_front()
        elif choice == 2:
            obj.remove_rear()
        elif choice == 3:
            break
        else:
            print("\n Please! Select your Right Option")

    obj.display()

# ---------------- Written By : - Aditya Pratap Singh ------------------

'''Applications of Deque Data Structure : ------->
   1. In undo operations on software.
   2. To store history in browsers.'''