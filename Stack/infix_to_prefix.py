"""
Python program to convert infix to prefix expression

Step 1: Reverse the infix expression i.e A+B*C will become C*B+A. Note while reversing each ‘(‘ will become ‘)’ and each ‘)’ becomes ‘(‘.
Step 2: Obtain the “nearly” postfix expression of the modified expression i.e CB*A+.
Step 3: Reverse the postfix expression. Hence in our example prefix is +A*BC.
"""
import traceback


class InfixToPostfix:
    def __init__(self):
            self.top = -1
            self.stack = []
            self.postfix = []
            #Setting precedence order
            self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isEmpty(self):
        """
        check if the stack is empty
        """
        if self.top == -1:
            return True
        return False

    def peek(self):
        """
        Returns the number at the top of the stack
        """
        return self.stack[-1]

    def pop(self):
        """
        Pops the element from the stack
        """
        if not self.isEmpty():
            self.top -= 1
            return self.stack.pop()
        else:
            raise Exception("Stack Underflow")

    def push(self, op):
        """
        Pushes the element to stack
        """
        self.top += 1
        self.stack.append(op)

    def is_operand(self, op):
        if op.isalpha():
            return True
        return False

    def not_greater(self, op):
        if self.precedence[op] <= self.precedence[self.peek()]:
            return True
        return False

    def infix_to_postfix(self, exp):
        """
        Main method to convert infix expression to postfix expression
        :param exp: string of infix expression
        :return: string postfix expression
        """

        try:
            for i in exp:
                #if the character is an operand output it
                if self.is_operand(i):
                    self.postfix.append(i)

                #if the character is '(' push it
                elif i is '(':
                    self.push('(')

                elif i is ')':
                    #if the character is ')" pop until we encounter '(' in the stack
                    while not self.isEmpty() and self.peek() is not '(':
                        self.postfix.append(self.pop())
                    if not self.isEmpty() and self.peek() is not '(':
                        return -1
                    else:
                        self.pop()

                #if an operator is encountered
                else:
                    while not self.isEmpty() and self.peek() is not '(' and self.not_greater(i):
                        self.postfix.append(self.pop())
                    self.push(i)
            while not self.isEmpty():
                self.postfix.append(self.pop())

            return ''.join(self.postfix)

        except Exception as e:
            print("Error occurred while performing infix to postfix conversion :", e)
            traceback.print_exc()
            return -1


if __name__=='__main__':
    infix = "(A-B/C)*(A/K-L)"
    infix = infix[::-1]
    infix = infix.replace('(', '<')
    infix = infix.replace(')', '>')
    infix = infix.replace('<', ')')
    infix = infix.replace('>', '(')
    convert = InfixToPostfix()
    postfix = convert.infix_to_postfix(infix)
    if postfix == -1:
        print("Error while performing coversion")
    else:
        print("prefix expression:", postfix[::-1])
