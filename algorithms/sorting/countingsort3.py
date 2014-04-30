#!/usr/bin/env python

if __name__ == "__main__":
    n = int(raw_input().strip())
    count = [0] * 100
    for i in xrange(n):
        line = raw_input().strip().split()
        count[int(line[0])] += 1
    output = 0
    for i in xrange(100):
        output += count[i]
        print output,
    print ""
