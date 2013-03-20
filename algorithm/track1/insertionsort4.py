#!/bin/python

# Head ends here
def insertionSort(ar):
    for i in range(1, len(ar)):
        j = i - 1
        v = ar[i]
        while j >= 0:
            if v < ar[j]:
                ar[j+1] = ar[j]
                ar[j] = v
                j = j - 1
            else:
                break
        print ' '.join([`num` for num in ar])

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
