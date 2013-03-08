#!/usr/bin/env python

def pairs(ar):
    ar = sorted(ar)
    count = 0
    for i in range(0, len(ar) - 1):
        for j in range(i+1, len(ar)):
            if ar[j] - ar[i] == 2:
                count += 1
            elif ar[j] - ar[i] > 2:
                break
    print count

(n, k) = (int(i) for i in raw_input().strip().split())
ar = [int(i) for i in raw_input().strip().split()]
pairs(ar)
