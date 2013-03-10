#!/usr/bin/env python

import random


def coordsToNum(tup):
    return 3 * tup[0] + 1 * tup[1]


def numberToCoords(n):
    return (n / 3 % 3, n % 3)


def convertInput(board):
    x = []
    o = []
    for i in xrange(0, 3):
        for j in xrange(0, 3):
            if board[i][j] is 'X':
                x.append(coordsToNum((i, j)))
            if board[i][j] is 'O':
                o.append(coordsToNum((i, j))) 
    return (x, o)


def getEmptySpaces(x, o):
    spases = range(0, 9) 
    for element in x + o:
        spases.remove(element)
    return spases 


def randomAnEmptySpace(x, o):
    emptySpaces = getEmptySpaces(x, o)
    return emptySpaces[random.randint(0, len(emptySpaces) - 1)]


def getWinPosition(p1, p2):
    (x1, y1) = p1 
    (x2, y2) = p2
    if x1 == x2:
        return coordsToNum((x1, 3 - y1 -y2))
    elif y1 == y2:
        return coordsToNum((3 - x1 - x2, y1))
    elif x1 == y1 and x2 == y2 or x1 + y1 == 2 and x2 + y2 == 2:
        return coordsToNum((3 - x1 - x2, 3 - y1 - y2)) 


def getWinPositions(x):
    result = []
    if len(x) < 2:
        return result
    for i in xrange(0, len(x)):
        for j in xrange(i + 1, len(x)):
            winPosition = getWinPosition(numberToCoords(x[i]), numberToCoords(x[j]))
            if winPosition is not None:
                result.append(winPosition)
    return result


def getLosePositions(o):
    return getWinPositions(o)


def nextMove(player, board):
    (x, o) = convertInput(board)
    emptyPositions = set(getEmptySpaces(x, o))
    winPositions = set(getWinPositions(x))
    losePositions = set(getLosePositions(o))
    if player is 'X':
        pass
    elif player is 'O':
        winPositions, losePositions = losePositions, winPositions
    intersect1 = emptyPositions & winPositions
    intersect2 = emptyPositions & losePositions
    coords = ()
    if intersect1:
        coords = numberToCoords(intersect1.pop()) 
    elif intersect2:
        coords = numberToCoords(intersect2.pop()) 
    else:
        coords = numberToCoords(randomAnEmptySpace(x, o))
    print coords[0], coords[1]


#If player is X, I'm the first player.
#If player is O, I'm the second player.
player = raw_input()

#Read the board now. The board is a 3x3 array filled with X, O or _.
board = []
for i in xrange(0, 3):
    board.append(raw_input())

nextMove(player,board)
