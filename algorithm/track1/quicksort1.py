#!/bin/python

# Head ends here
def partition(ar):
    p = 0
    for j in range(1, len(ar)):
        if ar[j] < ar[p]:
            ar = ar[0:p] + [ar[j]] + ar[p:j] + ar[j+1:]
            p += 1
    print ' '.join([`num` for num in ar])

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
