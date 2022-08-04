class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    # Push element on the Stack
    def push(self, data):
        self.top += 1
        self.stack.append(data)

    # Pop element on the Stack
    def pop(self):
        if self.top == -1:
            print("\n ---------> Stack is empty !")
        else:
            print("Popped Element = ", self.stack[self.top])
            self.stack.pop()
            self.top -= 1

    # Peek element on a Stack
    def peek(self):
        if self.top == -1:
            print("\n Here Top = -1 (Stack Empty) !")
        else:
            return self.stack[self.top]

    # Display a Stack
    def display(self):
        print("\n ****************** Display Stack ***************")
        if self.top == -1:
            print("\n --------> Stack is Empty !")
        else:
            for i in range(self.top, -1, -1):
                if i == self.top:
                    print(self.stack[i], "<----- Top")
                else:
                    print(self.stack[i])
                print("-----")


if __name__ == "__main__":
    obj = Stack()
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
