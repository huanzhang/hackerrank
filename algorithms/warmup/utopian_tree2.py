#!/usr/bin/env python

def utopian_height(n):
    if n == 0:
        return 1
    if n % 2:
        return utopian_height(n-1) * 2
    else:
        return utopian_height(n-1) + 1

if __name__ == "__main__":
    T = int(raw_input())
    N = [int(raw_input()) for x in range(T)]
    for n in N:
        print utopian_height(n)
