"""
NEXT GREATER ELEMENT
"""


def next_greater_element(array):
    stack = []
    nge = {}
    stack.append(array[0])
    for i in range(1,len(array)):
        while len(stack)>0 and array[i] > stack[-1]:
            nge[stack.pop()] = array[i]

        stack.append(array[i])

    while len(stack) > 0:
        nge[stack.pop()] = -1

    return nge

if __name__=='__main__':

    array = [11, 13, 21, 3]

    nge = next_greater_element(array)

    print(nge)


