#!/bin/python

# Head ends here
def insertionSort(ar): 
    result = ""
    t = ar[-1]
    for i in range(len(ar) - 2, -2, -1):
        if i is not -1:
            if ar[i] > t:
                ar[i + 1] = ar[i]
                if result is "":
                    result += str(ar)
                else:
                    result += "\n" + str(ar)
            else:
                ar[i + 1] = t
                if result is "":
                    result += str(ar)
                else:
                    result += "\n" + str(ar)
                break
        else:
            ar[0] = t
            if result is "":
                result += str(ar)
            else:
                result += "\n" + str(ar)
    result = result.replace("[", "")
    result = result.replace("]", "")
    result = result.replace(",", "")
    print result

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
