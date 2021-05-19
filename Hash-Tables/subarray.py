"""
Python program to find if an array is subset of another
"""

def is_subarray(arr1, arr2):

    freq = {}
    for i in range(len(arr1)):
        if freq.get(arr1[i]):
            freq[arr1[i]] += 1
        else:
            freq[arr1[i]] = 1

    for i in range(len(arr2)):
        if freq.get(arr2[i])and freq[arr2[i]] > 0:
            freq[arr2[i]] -= 1
        else:
            return False

    return True

if __name__=='__main__':

    arr1 = [ 11, 1, 13, 21, 3, 7 ]
    arr2 = [ 11, 3, 7, 1 ]

    if not is_subarray(arr1, arr2):
        print("arr2 is not subset of arr1")
    else:
        print("arr2 is subset of arr1")

        
        
