# -*- coding: utf-8 -*-
# @Time    : 6/12/18 8:47 AM

import random


def monte_carlo_circle(times=1000000):
    k = 0
    for i in range(times):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if (x**2 + y**2) < 1:
            k += 1
    return 4*(k/times)


if __name__ == '__main__':
    print(monte_carlo_circle())
