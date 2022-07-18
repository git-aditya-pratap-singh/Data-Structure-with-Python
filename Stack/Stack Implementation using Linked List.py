class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    # push element on the Stack
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    # pop element on the Stack
    def pop(self):
        if self.head is None:
            print("\n Stack is empty !")
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

    def peek(self):
        if self.head is None:
            print("\n Stack is empty !")
        else:
            return self.head.data

    # Display the Stack
    def display(self):
        print("\n ****************** Display Stack ***************")
        temp = self.head
        while temp:
            print(temp.data, end="<----")
            temp = temp.next


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
            print("Popped element : ", obj.pop())
        else:
            break
    obj.display()
    print("\n Top Element on stack : ", obj.peek())

# ---------------- Written By : - Aditya Pratap Singh ------------------
