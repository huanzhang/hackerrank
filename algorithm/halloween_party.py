#!/usr/bin/env python

def pieces(K):
    x = K / 2
    y = K - x
    return x * y

if __name__ == "__main__":
    T = int(raw_input())
    tests = []
    for i in range(T):
        tests.append(int(raw_input()))
    for K in tests:
        print pieces(K)
