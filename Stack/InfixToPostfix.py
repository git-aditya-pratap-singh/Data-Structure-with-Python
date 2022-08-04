# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Stack class
class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
    
    def push(self, item):
        if len(self.stack) < self.size:
            self.stack.append(item)           

    def pop(self):
        result = -1

        if self.stack != []:
            result = self.stack.pop()

        return result
    
    def display(self):
        if self.stack == []:
            print("Stack is empty!")
        else:
            print("Stack data:")
            for item in reversed(self.stack):
                print(item)
    
    def isEmpty(self):
        return self.stack == []
    
    def topChar(self):
        result = -1

        if self.stack != []:
            result = self.stack[len(self.stack) - 1]

        return result

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Aux operations
def isOperand(c):
    return c >= 'A' and c <= 'Z'

operators = "+-*/^"

def isOperator(c):
    return c in operators

def getPrecedence(c):
    result = 0

    for char in operators:
        result += 1

        if char == c:
            if c in '-/':
                result -= 1
            break

    return result

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# infix to postfix
def toPostfix(expression):
    result = ""

    stack = Stack(15)

    for char in expression:
        if isOperand(char):
            result += char
        elif isOperator(char):
            while True:
                topChar = stack.topChar()

                if stack.isEmpty() or topChar == '(':
                    stack.push(char)
                    break
                else:
                    pC = getPrecedence(char)
                    pTC = getPrecedence(topChar)

                    if pC > pTC:
                        stack.push(char)
                        break
                    else:
                        result += stack.pop()

        elif char == '(':
            stack.push(char)
        elif char == ')':
            cpop = stack.pop()

            while cpop != '(':
                result += cpop
                cpop = stack.pop()

    while not stack.isEmpty():
        cpop = stack.pop()
        result += cpop

    return result

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# test
infixExps = [
    'A*B+C',    # AB*C+
    'A+B*C',    # ABC*+ 
    'A*B+C*D',  # AB*CD*+
    'A*B^C+D',  # ABC^*D+ 
    'A*(B+C*D)+E',          # ABCD*+*E+  
    'A+(B*C-(D/E^F)*G)*H',  # ABC*DEF^/G*-H*+
    '(A+B)*C+D/(E+F*G)-H',  # AB+C*DEFG*+/+H-
    'A-B-C*(D+E/F-G)-H'     # AB-CDEF/+G-*-H-
]

for exp in infixExps:
    postfix = toPostfix(exp)
    print(f'Infix: {exp} -> Postfix: {postfix}')