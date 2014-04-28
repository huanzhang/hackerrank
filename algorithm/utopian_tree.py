#!/usr/bin/env python

def utree_height(n):
    h = 1
    for x in range(1, n+1):
        if x % 2:
            h = h * 2
        else:
            h = h + 1
    return h

if __name__ == '__main__':
    T = int(raw_input())
    N = [int(raw_input()) for x in range(T)]
    for n in N:
        print utree_height(n)
        
