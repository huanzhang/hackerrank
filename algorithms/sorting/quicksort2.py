#!/bin/python

# Head ends here
def quickSort(ar):
    if len(ar) is 0:
        return ar
    p = 0
    for j in range(1, len(ar)):
        if ar[j] < ar[p]:
            ar = ar[0:p] + [ar[j]] + ar[p:j] + ar[j+1:]
            p += 1
    if p < 2 and len(ar) - p < 3:
        if len(ar) > 1:
            print ' '.join([`num` for num in ar])
        return ar
    result =  quickSort(ar[0:p]) + [ar[p]] + quickSort(ar[p+1:])
    print ' '.join([`num` for num in result])
    return result

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)
