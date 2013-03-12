#!/bin/python


from random import choice


def money_left(first_moves, second_moves):
    money_left_p1 = 100
    money_left_p2 = 100
    draw_bids = []
    for (x, y) in zip(first_moves, second_moves):
        if x > y:
            money_left_p1 -= x
        elif y > x:
            money_left_p2 -= y
        else:
            draw_bids.append((x, y))
    for i in range(0, len(draw_bids)):
        if i & 1:
            money_left_p2 -= draw_bids[i][0]
        else:
            money_left_p1 -= draw_bids[i][0]
    return (money_left_p1, money_left_p2)


def has_draw_advantage(player, first_moves, second_moves):
    draw_bids = []
    for (x, y) in zip(first_moves, second_moves):
        if x == y:
            draw_bids.append((x, y))
    if player is 1:
        return (len(draw_bids) & 1) == 0
    if player is 2:
        return (len(draw_bids) & 1) == 1


def calculate_bid(player, pos, first_moves, second_moves):
    """the logic"""
    my_left= 0
    opposite_left= 0
    moves_to_win = 0
    is_my_draw_advantage = has_draw_advantage(player, first_moves, second_moves)
    opposite_moves = []
    if player is 1:
        my_left, opposite_left = money_left(first_moves, second_moves)
        moves_to_win = pos
        opposite_moves = second_moves
    else:
        opposite_left, my_left = money_left(first_moves, second_moves)
        moves_to_win = 10 - pos
        opposite_moves = first_moves
    # debug
    # print 'My left money: ' + str(my_left)
    # print 'Opposite left money: ' + str(opposite_left)
    # print 'Moves to win: ' + str(moves_to_win)
    # print 'Is my draw advantage: ' + str(is_my_draw_advantage)
    # the strategy/algorithm starts
    if is_my_draw_advantage and my_left >= (opposite_left+1)*(moves_to_win-1)+opposite_left:
        return opposite_left
    if not is_my_draw_advantage and my_left >= (opposite_left+1)*moves_to_win:
        return opposite_left+1
    if moves_to_win == 1:
        return my_left
    if moves_to_win == 2:
        return max(1, choice([my_left/5, my_left/3]))
    if 3 <= moves_to_win <= 7:
        if len(opposite_moves) != 0:
            return max(1, choice([my_left/20, my_left/15, min(my_left, sum(opposite_moves)/len(opposite_moves))]))
        else:
            return max(1, choice([my_left/30, my_left/20, my_left/15, my_left/15]))
    if moves_to_win == 8:
        return max(1, choice([my_left/5, my_left/3]))
    if moves_to_win == 9:
        if is_my_draw_advantage:
            if my_left >= opposite_left:
                return max(1, choice([opposite_left/2, opposite_left, opposite_left, opposite_left]))
        if not is_my_draw_advantage:
            if my_left > opposite_left:
                return max(1, choice([opposite_left/2, opposite_left+1, opposite_left+1, opposite_left+1]))
    return max(1, my_left/2)


#gets the id of the player
player = input()
scotch_pos = input()         #current position of the scotch

first_moves = [int(i) for i in raw_input().split()]
second_moves = [int(i) for i in raw_input().split()]
bid = calculate_bid(player,scotch_pos,first_moves,second_moves)
print bid
