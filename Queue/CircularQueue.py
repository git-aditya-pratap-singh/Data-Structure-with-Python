class CircularQueue:
    def __init__(self, size):
        self.queue = [None]*size
        self.size = size
        self.front = -1
        self.rear = -1

    # Insert Element into the Circular Queue
    def enqueue(self, data):
        if (self.rear+1) % self.size == self.front:
            print("\n The Circular Queue is full (Overflow) ! ")

        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data

        else:
            self.rear = (self.rear+1) % self.size
            self.queue[self.rear] = data

    # Delete Element into the Circular Queue
    def dequeue(self):
        if self.front == -1:
            print("\n The Circular Queue is empty (Underflow) !")

        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp

        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    # Display Element in CircularQueue
    def display(self):
        print("\n ******* Circular Queue ********")
        if self.front == -1:
            print("\n The Circular Queue is empty !")

        elif self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" | ")

        else:
            for j in range(0, self.rear+1):
                print(self.queue[j], end=" | ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" | ")
            print()


if __name__ == "__main__":
    size = int(input("\n Enter the Number of Array Size : "))
    obj = CircularQueue(size)
    num = 0
    while num >= 0:
        num = int(input("\n Enter the Number into CircularQueue : "))
        if num < 0:
            break
        else:
            obj.enqueue(num)
    obj.display()

    while True:
        print("\n Please ! Select Your Choice : Y/N ")
        check = input("\n Are You Sure Delete item into Queue : ")
        if check == 'Y':
            print("---->", obj.dequeue())
        else:
            break
    obj.display()

    while True:
        print("\n Please ! Select Your Choice : Y/N ")
        check = input("\n Are You Sure Insert item into Queue : ")
        if check == 'Y':
            num2 = int(input("\n Enter the Number into CircularQueue : "))
            obj.enqueue(num2)
        else:
            break
    obj.display()

# ---------------- Written By : - Aditya Pratap Singh ------------------

'''Applications of Circular Queue : --------->
   1. CPU scheduling
   2. Memory management
   3. Traffic Management'''
