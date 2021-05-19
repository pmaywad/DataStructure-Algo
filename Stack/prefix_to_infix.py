"""
Python program to convert prefix expression to an infix expression
Algorithm for Prefix to Infix:

Read the Prefix expression in reverse order (from right to left)
If the symbol is an operand, then push it onto the Stack
If the symbol is an operator, then pop two operands from the Stack
Create a string by concatenating the two operands and the operator between them.
string = (operand1 + operator + operand2)
And push the resultant string back to Stack
Repeat the above steps until end of Prefix expression.
"""

OPERATOR = "*/+-"

def prefix_to_infix(exp):
    exp = exp[::-1]
    stack = []
    for i in exp:
        if i not in OPERATOR:
            stack.append(i)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(f'({operand1}{i}{operand2})')

    return stack.pop()

if __name__=='__main__':
    prefix = "*-A/BC-/AKL"
    print(prefix_to_infix(prefix))

