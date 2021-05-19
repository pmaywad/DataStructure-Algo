"""
Python program to convert postfix expression to an infix expression

Algorithm
1.While there are input symbol left
…1.1 Read the next symbol from the input.
2.If the symbol is an operand
…2.1 Push it onto the stack.
3.Otherwise,
…3.1 the symbol is an operator.
…3.2 Pop the top 2 values from the stack.
…3.3 Put the operator, with the values as arguments and form a string.
…3.4 Push the resulted string back to stack.
4.If there is only one value in the stack
…4.1 That value in the stack is the desired infix string.
"""

OPERATOR = "*/+-"

def postfix_to_infix(exp):
    stack = []
    for i in exp:
        if i not in OPERATOR:
            stack.append(i)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(f'({operand2}{i}{operand1})')

    return stack.pop()

if __name__=='__main__':
    postfix = "AB+CD-*"
    print(postfix_to_infix(postfix))
