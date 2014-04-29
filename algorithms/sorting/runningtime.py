#!/bin/python

# Head ends here
def insertionSort(ar):
    shifts = 0
    for j in range(1, len(ar)):
        tmp = ar[j]
        for i in range(j - 1, -1, -1):
            if ar[i] > tmp:
                ar[i + 1] = ar[i]
                shifts += 1
            else:
                ar[i + 1] = tmp
                break
            if i is 0:
                ar[0] = tmp
    print shifts

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
