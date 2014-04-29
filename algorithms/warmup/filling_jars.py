#!/usr/bin/env python

def fill_jars(jars, a, b, k):
    for i in range(a-1, b):
        jars[i] = jars[i] + k

if __name__ == "__main__":
    (N, M) = [int(x) for x in raw_input().split()]
    opts = []
    for i in range(M):
        opts.append(tuple([int(x) for x in raw_input().split()]))
    jars = [0] * N
    for (a, b, k) in opts:
        fill_jars(jars, a, b, k)
    print sum(jars) / len(jars)
