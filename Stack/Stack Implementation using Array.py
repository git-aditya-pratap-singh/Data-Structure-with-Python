class Stack:
    def __init__(self, size):
        self.arr = [None]*size
        self.top = -1
        self.size = size

    # Push element on the stack
    def push(self, data):
        if self.top == self.size-1:
            print("\n Stack if full (Overflow) !")
        else:
            self.top += 1
            self.arr[self.top] = data

    # pop element on the stack
    def pop(self):
        if self.top == -1:
            print("\n Stack is empty !")
        else:
            print("popped elements : ", self.arr[self.top])
            self.top -= 1

    # Peek element on the Stack
    def peek(self):
        if self.top == -1:
            print("\n Here Top = -1 (Stack Empty) !")
        else:
            return self.arr[self.top]

    # display a Stack
    def display(self):
        if self.top == -1:
            print("\n Stack is empty !")
        else:
            print("\n ******** Stack ********")
            for i in range(self.top, -1, -1):
                if i == self.top:
                    print(self.arr[i], "<----- Top")
                else:
                    print(self.arr[i])
                print("-----")


if __name__ == "__main__":
    size_arr = int(input("\n Enter the size of Array : "))
    obj = Stack(size_arr)
    num = 0
    while num >= 0:
        num = int(input("\n Enter the Number into Stack : "))
        if num < 0:
            break
        else:
            obj.push(num)
    obj.display()
    print("\n Top Element on stack : ", obj.peek())

    while True:
        print("\n Please ! Select Your Choice : Y/N ")
        check = input("\n Are You Sure Delete item into Stack : ")
        if check == 'Y':
            obj.pop()
        else:
            break
    obj.display()
    print("\n Top Element on stack : ", obj.peek())

# ---------------- Written By : - Aditya Pratap Singh ------------------