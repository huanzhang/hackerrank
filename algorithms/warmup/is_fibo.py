#!/usr/bin/env python

def is_fibo(n):
    if n == 0:
        return True
    a = 0 
    b = 1
    while(b < n):
        (a, b) = (b, a+b)
    if b == n:
        return True
    else:
        return False

if __name__ == "__main__":
    t = int(raw_input().strip()) 
    candies = [int(raw_input().strip()) for x in range(t)]
    for c in candies:
        if is_fibo(c):
            print "IsFibo"
        else:
            print "IsNotFibo"
