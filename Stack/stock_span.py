"""
The Stock Span Problem

"""

def calcualte_span(price):
    """
    Calculates the span list
    :param price: list of stock prices for n consecutive days
    :return: span list
    """
    if not price:
        return []
    n = len(price)
    span = [0]*n
    stack = []
    span[0] = 1   #span for fisrt day will always be 1
    stack.append(0) #pushing first element in price to stack
    #Compute span for rest of the days
    for i in range(1,n):
        span[i] = 1
        while len(stack)>0 and price[stack[-1]] < price[i]:
            stack.pop()

        #if stack becomes empty then the price at i is greater than all the prices in left to it, else price[i] is greater than i - (top of stack)
        if len(stack) is 0:
            span[i] = i + 1
        else:
            span[i] = i - stack[-1]

        stack.append(i)

    return span


if __name__=='__main__':

    price = [10, 4, 5, 90, 120, 80]

    span = calcualte_span(price)

    print(span) #output: [1, 1, 2, 4, 5, 1]
    
    
