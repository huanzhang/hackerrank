#!/usr/bin/env python

def largest_decent(N):
    """ Return the number of `3` """
    for n in range(0, N + 1, 5):
        if not (N - n) % 3:
            return n
    return -1

if __name__ == "__main__":
    T = int(raw_input())
    tests = []
    for i in range(T):
        tests.append(int(raw_input()))
    for N in tests:
        n = largest_decent(N)
        if n != -1:
            print '5' * (N - n) + '3' * n
        else:
            print '-1'
