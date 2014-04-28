#!/usr/bin/env python

import bisect

def pairs(ar, k):
    """
    Algorithm: Binary Search
    """
    ar.sort()
    count = 0
    for i in range(0, len(ar) - 1):
        item_insert_point = bisect.bisect(ar, ar[i]-k)
        if ar[item_insert_point-1:item_insert_point] == [ar[i]-k]:
            count += 1
        item_insert_point = bisect.bisect(ar, ar[i]+k)
        if ar[item_insert_point-1:item_insert_point] == [ar[i]+k]:
            count += 1
    print count/2

(n, k) = (int(i) for i in raw_input().strip().split())
ar = [int(i) for i in raw_input().strip().split()]
pairs(ar, k)
