#!/bin/python

# Head ends here
def insertionSort(ar):
    """Insert element into sorted list
    """
    j = len(ar)-2
    value = ar[len(ar)-1]
    while j >= 0:
        if value < ar[j]:
            ar[j+1] = ar[j]
            print ' '.join([`num` for num in ar])
            ar[j] = value
            j = j - 1
        else:
            print ' '.join([`num` for num in ar])
            break

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
