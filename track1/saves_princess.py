#!/bin/python
# Head ends here
def nextMove(m,grid):
    four_corners = [(x, y) for x in [0, m-1] for y in [0, m-1]]
    princess = ()
    for x, y in four_corners:
        if grid[x][y] is not '-':
            princess = (x, y)
    bot = ((m - 1) / 2, (m - 1) / 2)
    vertical = ''
    horizontal = ''
    if princess is bot:
        return ""
    if princess[0] < bot[0]:
        vertical = 'UP'
    else:
        vertical = 'DOWN'
    if princess[1] < bot[1]:
        horizontal = 'LEFT'
    else:
        horizontal = 'RIGHT'
    directions = (vertical, horizontal)
    output = (('\n'.join(directions) + '\n') * ((m - 1) / 2)).rstrip()
    return output

# Tail starts here
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

print nextMove(m,grid)
