class PriorityQueue:
    def __init__(self, size):
        self.queue = [None]*size
        self.size = size

    def enqueue(self, data):
        pass

    def dequeue(self):
        pass

    def display(self):
        pass


if __name__ == "__main__":
    size = int(input("\n Enter the Size of Array (Priority Queue) : "))
    obj = PriorityQueue(size)
    num = 0
    while num >= 0:
        num = int(input("\n Enter the Numbers into Priority Queue : "))
        if num < 0:
            break
        else:
            obj.enqueue(num)
    obj.display()

# ---------------- Written By : - Aditya Pratap Singh ------------------
