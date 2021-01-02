# coding: utf-8
"""
    :copyright: (c) 2020 by Jon Thornton.
"""
import logging
import os

def main():
    treemap = []
    with open('input.txt', 'r') as file:
        treemap = [line.strip() for line in file]

    count = count_trees(treemap, 0, 1, 1) \
        * count_trees(treemap, 0, 3, 1) \
        * count_trees(treemap, 0, 5, 1) \
        * count_trees(treemap, 0, 7, 1) \
        * count_trees(treemap, 0, 1, 2)
    print(count)


def count_trees(treemap, start_x, incr_x, incr_y):
    count = 0
    y = incr_y
    x = start_x + incr_x

    while y < len(treemap):
        if treemap[y][x] == '#':
            count += 1

        y += incr_y
        x = (x + incr_x) % len(treemap[0])

    return count


if __name__ == '__main__':
    main()
