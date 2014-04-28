#!/usr/bin/env python

def largest_vehicle(width, i, j):
    min = width[j]
    for x in range(i, j):
        if width[x] < min:
            min = width[x]
    return min


if __name__ == "__main__":
    (N, T) = [int(x) for x in raw_input().split()]
    width = [int(x) for x in raw_input().split()]
    test_cases = []
    for t in range(T):
        test_cases.append(tuple( [int(x) for x in raw_input().split()]))
    for (i, j) in test_cases:
        print largest_vehicle(width, i, j)
