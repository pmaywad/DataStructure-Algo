"""
Check for Balanced Brackets in an expression using Stack

Declare a character stack S.
Now traverse the expression string exp. 
If the current character is a starting bracket (‘(‘ or ‘{‘ or ‘[‘) then push it to stack.
If the current character is a closing bracket (‘)’ or ‘}’ or ‘]’) then pop from stack and if the popped character is the matching starting bracket then fine else brackets are not balanced.
After complete traversal, if there is some starting bracket left in stack then “not balanced”
"""

OPENING_BRACKETS = "({["
CLOSING_BRACKETS = ")}]"

def are_brackets_balanced(exp):
    stack = []
    for i in exp:
        if i in OPENING_BRACKETS:
            stack.append(i)
        elif i in CLOSING_BRACKETS:
            top = stack.pop()
            if i is ')' and top is not '(':
                return False
            elif i is '}' and top is not '{':
                return False
            elif i is ']' and top is not '[':
                return False
    if len(stack) is not 0:
        return False

    return True

if __name__=='__main__':
    exp = '[()]{}{[()()]()}'
    balanced = are_brackets_balanced(exp)
    if balanced:
        print("Balanced Expression")
    else:
        print("Unbalanced Brackets")
        
        
