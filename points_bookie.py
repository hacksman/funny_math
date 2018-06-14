# -*- coding: utf-8 -*-
# @Time    : 6/14/18 7:51 AM

import random

__MAIN_WIN = "main_win"
__AID_WIN = "aid_win"


def create_bet(win_number, main_win_init, aid_win_init):
    main_win_count = main_win_init
    aid_win_count = aid_win_init

    total_count = main_win_init + aid_win_init

    while main_win_count != win_number and aid_win_count != win_number:
        total_count += 1
        win_random = random.randint(0, 1)
        if win_random == 0:
            main_win_count += 1
        else:
            aid_win_count += 1

    if main_win_count > aid_win_count:
        return __MAIN_WIN
    if main_win_count < aid_win_count:
        return __AID_WIN


def allot_bookie(n=10000, bookie_init=200, main_win_init=0, aid_win_init=0, win_number=3):
    main_win_count, aid_win_count = [0]*2
    for i in range(n):
        winner = create_bet(win_number, main_win_init, aid_win_init)
        if winner == __MAIN_WIN:
            main_win_count += 1
        else:
            aid_win_count += 1
    main_chance_win = main_win_count/n
    aid_chance_win = aid_win_count/n

    return bookie_init*main_chance_win, bookie_init*aid_chance_win


if __name__ == '__main__':
    print(allot_bookie(main_win_init=5, aid_win_init=2, win_number=10))


