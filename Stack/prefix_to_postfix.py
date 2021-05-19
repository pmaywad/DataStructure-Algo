"""
Python program to convert prefix expression to a postfix expression

Algorithm for Prefix to Postfix:

Read the Prefix expression in reverse order (from right to left)
If the symbol is an operand, then push it onto the Stack
If the symbol is an operator, then pop two operands from the Stack
Create a string by concatenating the two operands and the operator after them.
string = operand1 + operand2 + operator
And push the resultant string back to Stack
Repeat the above steps until end of Prefix expression.
"""

OPERATOR = "*/+-"

def prefix_to_postfix(exp):
    exp = exp[::-1]
    stack = []
    for i in exp:
        if i not in OPERATOR:
            stack.append(i)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(f'{operand1}{operand2}{i}')

    return stack[0]

if __name__=='__main__':
    prefix = "*-A/BC-/AKL"
    print(prefix_to_postfix(prefix)) #output ABC/-AK/L-*
