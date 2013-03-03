#!/bin/python
# Head ends here
def nextMove(n,x,y,grid):
    all_positions = [(i, j) for i in xrange(0, n) for j in xrange(0, n)]
    princess = () 
    for (i, j) in all_positions:
        if grid[i][j] is 'p':
            princess = (i, j)
    result = ""
    if x < princess[0]:
        result = "DOWN" 
    elif x > princess[0]:
        result = "UP"
    elif y < princess[1]:
        result = "RIGHT"
    elif y > princess[1]:
        result = "LEFT"
    print result
# Tail starts here
n = input()
x,y = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

nextMove(n,x,y,grid)
