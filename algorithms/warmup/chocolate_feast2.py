#!/usr/bin/env python

def changed_chocolates(wrappers, M):
    if wrappers < M:
        return 0
    return wrappers/M + changed_chocolates(wrappers/M + wrappers%M, M)


if __name__ == "__main__":
    T = int(raw_input())
    tests = []
    for i in range(T):
        tests.append(tuple([int(x) for x in raw_input().split()]))
    for (N, C, M) in tests:
        print N/C + changed_chocolates(N/C, M)
