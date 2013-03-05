#!/bin/python

# Head ends here
def insertionSort(ar):
        tmp = ar[-1]
        for i in range(len(ar) - 2, -1, -1):
            if ar[i] > tmp:
                ar[i + 1] = ar[i]
                print ' '.join([`num` for num in ar])
            else:
                ar[i + 1] = tmp
                print ' '.join([`num` for num in ar])
                break
            if i is 0:
                ar[0] = tmp
                print ' '.join([`num` for num in ar])

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
