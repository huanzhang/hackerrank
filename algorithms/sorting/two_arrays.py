#!/usr/bin/python


def exists_the_arrange(A, B, n, k):
    for i in xrange(n):
        p = -1
        for j in xrange(i, n):
            if p == -1 and A[i] + B[j] >= k:
                p = j
            if p != -1 and A[i] + B[j] >= k and B[j] < B[p]:
                p = j
        if p != -1:
            B[i], B[p] = B[p], B[i]
        else:
            return False
    return True


if __name__ == "__main__":
    t = int(raw_input())
    for i in xrange(t):
        n, k = map(int, raw_input().strip().split())
        A = map(int, raw_input().strip().split())
        B = map(int, raw_input().strip().split())
        if exists_the_arrange(A, B, n, k):
            print "YES"
        else:
            print "NO"

