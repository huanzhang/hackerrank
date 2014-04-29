#!/usr/bin/env python

if __name__ == "__main__":
    n = int(raw_input())
    k = int(raw_input())
    candies = [int(raw_input()) for i in range(0,n)]
    candies.sort()
    min_diff = candies[k-1] - candies[0]
    for i in range(k, len(candies)):
        if candies[i] - candies[i-k+1] < min_diff:
            min_diff = candies[i] - candies[i-k+1]
    print min_diff
