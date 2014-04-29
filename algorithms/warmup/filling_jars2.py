#!/usr/bin/env python

if __name__ == "__main__":
    N, M = [int(x) for x in raw_input().strip().split()]
    T = []
    for i in range(M):
        T.append(tuple([int(x) for x in raw_input().strip().split()]))
    sum = 0
    for (a, b, k) in T:
        sum += (b - a + 1) * k
    print sum / N
