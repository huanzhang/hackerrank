#!/usr/bin/env python

def total_chocolates(N, C, M):
    bought = N/C
    wrappers = bought
    while(wrappers >= M):
        changed = wrappers/M
        remaining = wrappers % M
        bought += changed
        wrappers = changed + remaining
    return bought


if __name__ == "__main__":
    T = int(raw_input())
    tests = []
    for i in range(T):
        tests.append(tuple([int(x) for x in raw_input().split()]))
    for (N, C, M) in tests:
        print total_chocolates(N, C, M)
